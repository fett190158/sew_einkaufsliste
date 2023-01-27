from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datamodel import Base, ShoppingList, Product, Association

engine = create_engine('sqlite:///database.sql')
Base.metadata.create_all(engine)


def create_shopping_list(name: str, date: str):
    with Session(engine) as session:
        new_shoppinglist = ShoppingList(Name=name, Date=date)
        session.add(new_shoppinglist)
        session.commit()


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

    create_shopping_list(name="test123", date="morgen")
