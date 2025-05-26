import osmium
import geojson

class TrailWayHandler(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.features = []

    def way(self, w):
        if not w.nodes:
            return
        if w.tags.get('highway') in ['path', 'track', 'footway', 'steps', 'bridleway', 'cycleway']:
            try:
                coords = [(node.lon, node.lat) for node in w.nodes]
                props = dict(w.tags)
                props['id'] = w.id
                feature = geojson.Feature(
                    geometry=geojson.LineString(coords),
                    properties=props
                )
                self.features.append(feature)
            except Exception as e:
                print(f"⚠️ Skipped way {w.id} due to error: {e}")

# Run it
handler = TrailWayHandler()

# Important: make sure this file was downloaded using Overpass QL (with node data!)
handler.apply_file("trails.osm", locations=True)

# Save to GeoJSON
geo = geojson.FeatureCollection(handler.features)
with open("trails.geojson", "w", encoding="utf-8") as f:
    geojson.dump(geo, f, indent=2)

print(f"✅ Saved {len(handler.features)} trail features to trails.geojson")
