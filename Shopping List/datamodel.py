from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


ShoppingList_Product = Table(
    'ShoppingList_Product', Base.metadata,
    Column("Shopping_Lists_ID", Integer, ForeignKey("Shopping_List.ID"),
           primary_key=True),
    Column("Products_ID", Integer, ForeignKey("Product.ID"),
           primary_key=True))


class Product(Base):
    __tablename__ = "Product"

    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Quantity = Column(Integer)
    Volume = Column(Integer, nullable=True)
    Weight = Column(Integer, nullable=True)
    Shopping_Lists = relationship("ShoppingList",
                                  secondary=ShoppingList_Product,
                                  back_populates="Product")


class ShoppingList(Base):
    __tablename__ = "Shopping_List"

    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Date = Column(String)
    Products = relationship("Product", secondary=ShoppingList_Product,
                            back_populates="Shopping_Lists")
