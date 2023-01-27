from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Association(Base):
    __tablename__ = "Association_Table"
    Product_ID = Column(ForeignKey("Product.ID"), primary_key=True)
    Shoppinglist_ID = Column(ForeignKey("Shopping_List.ID"), primary_key=True)
    Shopping_List = relationship("ShoppingList", back_populates="Products")
    Product = relationship("Product", back_populates="Shopping_Lists")


class ShoppingList(Base):
    __tablename__ = "Shopping_List"

    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Date = Column(String)
    Products = relationship("Association", back_populates="Shopping_List")


class Product(Base):
    __tablename__ = "Product"

    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Volume = Column(String, nullable=True)
    Weight = Column(String, nullable=True)
    Shopping_Lists = relationship("Association", back_populates="Product")
