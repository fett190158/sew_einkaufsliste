from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datamodel import Base, ShoppingList

engine = create_engine('sqlite:///database.sql')
Base.metadata.create_all(engine)


def create_shopping_list(name, date):
    with Session(engine) as session:
        new_shoppinglist = ShoppingList(Name=name, Date=date)
        session.add(new_shoppinglist)
        session.commit()


if __name__ == '__main__':
    create_shopping_list("List1", "25.4.2019")