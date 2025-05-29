import pandas as pd
from sqlalchemy.orm import sessionmaker
from models import engine, Restaurant

df = pd.read_json("restaurants_cleaned.csv")  # or use CSV if available

Session = sessionmaker(bind=engine)
session = Session()

for _, row in df.iterrows():
    restaurant = Restaurant(
        name=row["Name"],
        rating=row["Rating"],
        food_type=row["Food Types"],
        address=row["Address"]
    )
    session.add(restaurant)

session.commit()
print("✅ Imported restaurants.")
