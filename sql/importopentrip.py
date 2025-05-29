import pandas as pd
import ast
from sqlalchemy.orm import sessionmaker
from models import engine, OpenTripPlace

df = pd.read_csv("opentrip_places_cleaned.csv")

df["point"] = df["point"].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else {"lat": None, "lon": None})

Session = sessionmaker(bind=engine)
session = Session()

for _, row in df.iterrows():
    place = OpenTripPlace(
        xid=row["xid"],
        name=row["name"],
        distance=row["dist"],
        rating=row["rate"],
        wikidata=row["wikidata"] if pd.notnull(row["wikidata"]) else None,
        kinds=row["kinds"],
        latitude=row["point"].get("lat"),
        longitude=row["point"].get("lon"),
        osm=row["osm"] if pd.notnull(row["osm"]) else None,
    )
    session.add(place)

session.commit()
print("✅ Imported OpenTrip places.")
