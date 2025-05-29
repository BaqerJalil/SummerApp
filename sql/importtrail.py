import pandas as pd
from sqlalchemy.orm import sessionmaker
from models import engine, TrailSegment

df = pd.read_csv("trail_segments_cleaned.csv")

Session = sessionmaker(bind=engine)
session = Session()

for _, row in df.iterrows():
    seg = TrailSegment(
        segment_id=row.get("ess"),  # unique ID
        start_lon=row.iloc[1],
        start_lat=row.iloc[2],
        end_lon=row.iloc[3],
        end_lat=row.iloc[4],
        length_m=row.iloc[5],
        original_way_id=row.iloc[-1] if pd.notnull(row.iloc[-1]) else None
    )
    session.add(seg)

session.commit()
print("✅ Imported trail segments.")
