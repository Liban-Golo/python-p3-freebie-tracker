from models.base import Base, engine
from models.company import Company
from models.dev import Dev
from models.freebie import Freebie

# Create all tables
Base.metadata.create_all(engine)
print("Tables created successfully!")
