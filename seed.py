from models.base import Session
from models.company import Company
from models.dev import Dev

session = Session()

# Create companies
company1 = Company(name="TechCorp", founding_year=2000)
company2 = Company(name="CodeLabs", founding_year=1995)
session.add_all([company1, company2])
session.commit()

# Create devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
session.add_all([dev1, dev2])
session.commit()

# Create freebies
company1.give_freebie(dev1, "Sticker", 5)
company1.give_freebie(dev2, "T-Shirt", 20)
company2.give_freebie(dev1, "Mug", 10)
company2.give_freebie(dev2, "Notebook", 15)

session.commit()
print("Seed data added successfully!")
