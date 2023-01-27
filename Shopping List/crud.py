from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from datamodel import Base, ShoppingList, Product, ShoppingList_Product

engine = create_engine('sqlite:///database.sql')
Base.metadata.create_all(engine)


def create_shopping_list(session: Session, name: str, date: str):
    new_shoppinglist = ShoppingList(Name=name, Date=date)
    session.add(new_shoppinglist)
    session.commit()
    return new_shoppinglist


def create_product(session: Session, name: str, quantity: int, volume: int,
                   weight: int):
    new_product = Product(Name=name, Quantity=quantity, Volume=volume,
                          Weight=weight)
    session.add(new_product)
    session.commit()
    return new_product


def add_product_to_shopping_list(session: Session, shopping_list: ShoppingList,
                                 product: Product):
    shopping_list.Products.append(product)
    session.commit()


if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    shopping_list = create_shopping_list(session, "Weekly Groceries",
                                         "2022.01.01")
    product = create_product(session, "Milk", 2, "1l", None)
    add_product_to_shopping_list(session, shopping_list, product)
    session.close()
