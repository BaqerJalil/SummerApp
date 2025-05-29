import pandas as pd
from sqlalchemy.orm import sessionmaker
from models import engine, TicketmasterEvent

df = pd.read_csv("ticketmaster_cleaned.csv")

Session = sessionmaker(bind=engine)
session = Session()

for _, row in df.iterrows():
    event = TicketmasterEvent(
        name=row["name"],
        date=row["date"],
        time=row["time"],
        venue=row["venue"],
        url=row["url"]
    )
    session.add(event)

session.commit()
print("✅ Imported Ticketmaster events.")
