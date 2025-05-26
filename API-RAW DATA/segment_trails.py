import geojson
import math
import hashlib
import pandas as pd

# --- Haversine formula for distance in meters ---
def haversine(coord1, coord2):
    from math import radians, sin, cos, sqrt, atan2
    lon1, lat1 = coord1
    lon2, lat2 = coord2
    R = 6371000
    dlon = radians(lon2 - lon1)
    dlat = radians(lat2 - lat1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# --- Bounding box for a segment ---
def get_bbox(points):
    lons = [pt[0] for pt in points]
    lats = [pt[1] for pt in points]
    return {
        "min_lon": min(lons), "max_lon": max(lons),
        "min_lat": min(lats), "max_lat": max(lats)
    }

# --- Load GeoJSON file ---
with open("trails.geojson", "r", encoding="utf-8") as f:
    data = geojson.load(f)

segments = []

# --- Create segments from line coordinates ---
for feature in data["features"]:
    coords = feature["geometry"]["coordinates"]
    tags = feature.get("properties", {})

    for i in range(len(coords) - 1):
        pt1 = coords[i]
        pt2 = coords[i + 1]
        distance = haversine(pt1, pt2)
        bbox = get_bbox([pt1, pt2])
        seg_id = hashlib.md5(f"{pt1}-{pt2}".encode()).hexdigest()

        segments.append({
            "segment_id": seg_id,
            "start_lon": pt1[0],
            "start_lat": pt1[1],
            "end_lon": pt2[0],
            "end_lat": pt2[1],
            "distance_m": round(distance, 2),
            "min_lat": bbox["min_lat"],
            "max_lat": bbox["max_lat"],
            "min_lon": bbox["min_lon"],
            "max_lon": bbox["max_lon"],
            "bicycle_access": tags.get("bicycle", "").lower().strip(),
            "private_access": tags.get("access", "").lower().strip(),
            "original_way_id": str(tags.get("id", "unknown")).strip()
        })

# --- Save raw data ---
df_raw = pd.DataFrame(segments)
df_raw.to_csv("trail_segments_raw.csv", index=False)

# --- Clean the data ---
df_clean = df_raw.copy()

# Normalize text fields
text_cols = ["bicycle_access", "private_access", "original_way_id"]
for col in text_cols:
    df_clean[col] = df_clean[col].fillna("unknown").astype(str).str.lower().str.strip()

# Convert coordinates/distance to float
coord_cols = ["start_lon", "start_lat", "end_lon", "end_lat", "distance_m",
              "min_lat", "max_lat", "min_lon", "max_lon"]
for col in coord_cols:
    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

# Handle missing: flag as 'missing' if still null
df_clean.fillna("missing", inplace=True)

# Deduplicate
df_clean.drop_duplicates(subset=["segment_id"], inplace=True)

# Save cleaned version
df_clean.to_csv("trail_segments_clean.csv", index=False)

print(f"✅ Saved {len(df_clean)} cleaned trail segments to trail_segments_clean.csv")
