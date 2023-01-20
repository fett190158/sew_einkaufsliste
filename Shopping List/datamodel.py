from sqlalchemy import Column, Integer, String, Date, ForeignKey    
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class ShoppingList(Base):
    __tablename__ = "Shopping_List"

    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Date = Column(Date)
    Product = relationship("Product")


class Product(Base):
    __tablename__ = "Product"

    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Quantity = Column(Integer)
    Volume = Column(Integer, nullable=True)
    Weight = Column(Integer, nullable=True)
    ShoppingList_ID = Column(Integer, ForeignKey("Shopping_List.ID"))
