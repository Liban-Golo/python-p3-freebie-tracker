from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Dev(Base):
    __tablename__ = "devs"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    freebies = relationship("Freebie", back_populates="dev")

    @property
    def companies(self):
        return list({freebie.company for freebie in self.freebies})

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev
