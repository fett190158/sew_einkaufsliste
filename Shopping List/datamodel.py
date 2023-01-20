from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


association_table = Table(
    "Association_Table",
    Base.metadata,
    Column("shoppinglist_id", ForeignKey("Shopping_List.id")),
    Column("product_id", ForeignKey("Product.id")),
    )


class ShoppingList(Base):
    __tablename__ = "Shopping_List"

    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Date = Column(Date)
    Product = relationship("Product", secondary=association_table)


class Product(Base):
    __tablename__ = "Product"

    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Quantity = Column(Integer)
    Volume = Column(Integer, nullable=True)
    Weight = Column(Integer, nullable=True)
