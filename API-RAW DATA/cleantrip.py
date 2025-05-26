import pandas as pd
import numpy as np

# Load raw data
raw_file = 'opentrip_places.csv'  # Change to your raw file path
df = pd.read_csv(raw_file)

# Save raw backup just in case
df.to_csv('opentrip_places_raw_backup.csv', index=False)

# --- Data Cleaning ---

# Normalize text fields: lowercase and strip whitespace for object/string columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.lower().str.strip()

# Handle missing data:
# Example: fill missing ratings with 0, or create flag columns for missing data
if 'rating' in df.columns:
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df['rating_missing'] = df['rating'].isna()
    df['rating'].fillna(0, inplace=True)

# Deduplicate rows
df.drop_duplicates(inplace=True)

# Normalize numeric columns (e.g., price, rating)
# Assuming rating already done; for price you can do similar:
if 'price' in df.columns:
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['price_missing'] = df['price'].isna()
    df['price'].fillna(df['price'].median(), inplace=True)  # or fill with median or 0

# Normalize dates if you have date columns
date_cols = [col for col in df.columns if 'date' in col.lower()]
for dcol in date_cols:
    df[dcol] = pd.to_datetime(df[dcol], errors='coerce')

# Normalize coordinates if available, e.g. lat, lon
if 'lat' in df.columns:
    df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
if 'lon' in df.columns:
    df['lon'] = pd.to_numeric(df['lon'], errors='coerce')

# Save cleaned data
df.to_csv('opentrip_places_cleaned.csv', index=False)

print(f"✅ Cleaning complete. Raw backup saved to 'opentrip_places_raw_backup.csv', cleaned data saved to 'opentrip_places_cleaned.csv'.")
