from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    # String reference to avoid circular import
    freebies = relationship("Freebie", back_populates="company")

    @property
    def devs(self):
        return list({freebie.dev for freebie in self.freebies})

    def give_freebie(self, dev, item_name, value):
        from .freebie import Freebie  # import inside method to avoid circular import
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        return new_freebie

    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()
