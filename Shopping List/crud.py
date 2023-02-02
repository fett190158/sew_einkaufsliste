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


def create_product(name: str, volume: str, weight: str):
    with Session(engine) as session:
        new_product = Product(Name=name, Volume=volume, Weight=weight)
        session.add(new_product)
        session.commit()


def associate_shopping_list_and_product(shopping_list_name: str, product_name: str):
    with Session(engine) as session:
        shopping_list = session.query(ShoppingList).filter_by(Name=shopping_list_name).first()
        product = session.query(Product).filter_by(Name=product_name).first()
        if shopping_list and product:
            association = Association(ShoppingList_ID=shopping_list.ID, Product_ID=product.ID)
            session.add(association)
            session.commit()
        else:
            print("Either Shopping List or Product does not exist.")


def read_shopping_lists():
    with Session(engine) as session:
        shopping_list = session.query(ShoppingList).all()
        return shopping_list


def read_products():
    with Session(engine) as session:
        products = session.query(Product).all()
        return products


def read_shopping_list_with_products(shopping_list_name: str):
    with Session(engine) as session:
        shopping_list = session.query(ShoppingList).filter_by(Name=shopping_list_name).first()
        shopping_list_id = shopping_list.ID
        assosiation = session.query(Association).filter_by(Shoppinglist_ID=shopping_list_id).all()
        product_ids = [assosiation.Shoppinglist_ID]
        print(product_ids)
        # product_id = assosiation.Product_ID
        # products = session.query(Product).filter_by(ID=product_id).all()


def read_shopping_list_with_products(shopping_list_name: str):
    with Session(engine) as session:
        shopping_list = session.query(ShoppingList).filter_by(Name=shopping_list_name).first()
        if shopping_list:
            shopping_list_products = [association.Product for association in shopping_list.Associations]
            return (shopping_list, shopping_list_products)
        else:
            print("Shopping List does not exist.")


def update_shopping_list_name(shopping_list_name: str, new_shopping_list_name):
    with Session(engine) as session:
        shopping_list = session.query(ShoppingList).filter_by(Name=shopping_list_name).first()
        if shopping_list:
            shopping_list.Name = new_shopping_list_name
            session.commit()
        else:
            print("Shopping List does not exist.")


def update_shopping_list_date(shopping_list_name: str, new_shopping_list_date):
    with Session(engine) as session:
        shopping_list = session.query(ShoppingList).filter_by(Name=shopping_list_name).first()
        if shopping_list:
            shopping_list.Date = new_shopping_list_date
            session.commit()
        else:
            print("Shopping List does not exist.")


def update_product_name(product_name:str, new_product_name):
    with Session(engine) as session:
        shopping_list = session.query(ShoppingList).filter_by(Name=product_name).first()
        if shopping_list:
            shopping_list.Name = new_product_name
            session.commit()
        else:
            print("Product does not exist.")


def update_product_volume(product_name:str, new_product_volume):
    with Session(engine) as session:
        shopping_list = session.query(ShoppingList).filter_by(Name=product_name).first()
        if shopping_list:
            shopping_list.Volume = new_product_volume
            session.commit()
        else:
            print("Product does not exist.")


def update_product_weight(product_name:str, new_product_weight):
    with Session(engine) as session:
        shopping_list = session.query(ShoppingList).filter_by(Name=product_name).first()
        if shopping_list:
            shopping_list.Weight = new_product_weight
            session.commit()
        else:
            print("Product does not exist.")


def delete_shopping_list(shopping_list_name: str):
    with Session(engine) as session:
        shopping_list = session.query(ShoppingList).filter_by(Name=shopping_list_name).first()
        if shopping_list:
            session.delete(shopping_list)
            session.commit()
        else:
            print("Shopping List does not exist.")


def delete_product(product_name: str):
    with Session(engine) as session:
        product = session.query(ShoppingList).filter_by(Name=product_name).first()
        if product:
            session.delete(product)
            session.commit()
        else:
            print("Product does not exist.")


if __name__ == '__main__':

    delete_shopping_list(shopping_list_name="test123")
    delete_product(product_name="Äpfel")
    create_shopping_list(name="test123", date="1.1.2022")
    create_product(name="Äpfel", volume=None, weight="1kg")
    associate_shopping_list_and_product(shopping_list_name="test123", product_name="Äpfel")
