from sqlalchemy import Column, Integer, String, Float, Date, Time, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)
    food_type = Column(String)
    address = Column(String)

class OpenTripPlace(Base):
    __tablename__ = 'opentrip_places'
    id = Column(Integer, primary_key=True, autoincrement=True)
    xid = Column(String)
    name = Column(String)
    distance = Column(Float)
    rating = Column(Float)
    wikidata = Column(String)
    kinds = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    osm = Column(String)

class TicketmasterEvent(Base):
    __tablename__ = 'ticketmaster_events'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)  # Use Date type if parsed
    time = Column(String)  # Use Time type if parsed
    venue = Column(String)
    url = Column(String)

class TrailSegment(Base):
    __tablename__ = 'trail_segments'
    id = Column(Integer, primary_key=True)
    segment_id = Column(String)
    start_lon = Column(Float)
    start_lat = Column(Float)
    end_lon = Column(Float)
    end_lat = Column(Float)
    length_m = Column(Float)
    original_way_id = Column(Integer)

try:
    engine = create_engine('sqlite:///db.sqlite3')
    Base.metadata.create_all(engine)
    print("✅ All models created successfully in db.sqlite3")
except Exception as e:
    print(f"❌ Error creating models: {e}")
