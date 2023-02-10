from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datamodel import Base, ShoppingList, Product, Association

engine = create_engine('sqlite:///database.sql')
Base.metadata.create_all(engine)


class Functions():

    def create_shopping_list(shopping_list_name, date):
        with Session(engine) as session:
            new_shoppinglist = ShoppingList(Name=shopping_list_name, Date=date)
            session.add(new_shoppinglist)
            session.commit()

    def create_product(product_name, volume, weight):
        with Session(engine) as session:
            new_product = Product(Name=product_name, Volume_in_l=volume,
                                  Weight_in_g=weight)
            session.add(new_product)
            session.commit()

    def create_product_in_shopping_list(product_name, volume, weight,
                                        shopping_list_id):
        with Session(engine) as session:
            if shopping_list_id:
                new_product = Product(Name=product_name, Volume_in_l=volume,
                                      Weight_in_g=weight)
                session.add(new_product)
                session.commit()
                new_product_id = new_product.ID
                association = Association(Shoppinglist_ID=shopping_list_id,
                                          Product_ID=new_product_id)
                session.add(association)
                session.commit()
            else:
                print("Shopping List does not exist.")

    def associate_shopping_list_and_product(shopping_list_id, product_id):
        with Session(engine) as session:
            if shopping_list_id and product_id:
                association = Association(Shoppinglist_ID=shopping_list_id,
                                          Product_ID=product_id)
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

    def read_products_of_shopping_list(shopping_list_id):
        with Session(engine) as session:
            shopping_list = session.query(ShoppingList) \
                            .filter_by(ID=shopping_list_id).first()
            if shopping_list:
                products = session.query(Product).join(Association,
                                                       Association.
                                                       Product_ID ==
                                                       Product.ID) \
                            .filter(Association.Shoppinglist_ID ==
                                    shopping_list.ID).all()
                print(f"{shopping_list.Name}")
                for product in products:
                    print(f"{product.Name} | Volume = {product.Volume_in_l} l \
                          | Weigth = {product.Weight_in_g} g")
                return products
            else:
                print("Shopping List does not exist.")

    def update_shopping_list_name(shopping_list_id, new_shopping_list_name):
        with Session(engine) as session:
            shopping_list = session.query(ShoppingList) \
                            .filter_by(ID=shopping_list_id).first()
            if shopping_list:
                shopping_list.Name = new_shopping_list_name
                session.commit()
            else:
                print("Shopping List does not exist.")

    def update_shopping_list_date(shopping_list_id: int,
                                  new_shopping_list_date):
        with Session(engine) as session:
            shopping_list = session.query(ShoppingList) \
                            .filter_by(ID=shopping_list_id).first()
            if shopping_list:
                shopping_list.Date = new_shopping_list_date
                session.commit()
            else:
                print("Shopping List does not exist.")

    def update_product_name(product_id, new_product_name):
        with Session(engine) as session:
            shopping_list = session.query(ShoppingList) \
                            .filter_by(ID=product_id).first()
            if shopping_list:
                shopping_list.Name = new_product_name
                session.commit()
            else:
                print("Product does not exist.")

    def update_product_volume(product_id, new_product_volume):
        with Session(engine) as session:
            shopping_list = session.query(ShoppingList) \
                            .filter_by(ID=product_id).first()
            if shopping_list:
                shopping_list.Volume_in_l = new_product_volume
                session.commit()
            else:
                print("Product does not exist.")

    def update_product_weight(product_id, new_product_weight):
        with Session(engine) as session:
            shopping_list = session.query(ShoppingList) \
                            .filter_by(ID=product_id).first()
            if shopping_list:
                shopping_list.Weight_in_g = new_product_weight
                session.commit()
            else:
                print("Product does not exist.")

    def delete_shopping_list(shopping_list_id):
        with Session(engine) as session:
            shopping_list = session.query(ShoppingList) \
                .filter_by(ID=shopping_list_id).first()
            if shopping_list:
                session.delete(shopping_list)
                session.commit()
            else:
                print("Shopping List does not exist.")

    def delete_product(product_id):
        with Session(engine) as session:
            product = session.query(Product).filter_by(ID=product_id).first()
            if product:
                session.delete(product)
                session.commit()
            else:
                print("Product does not exist.")

    def delete_product_from_shopping_list(shopping_list_id, product_id):
        with Session(engine) as session:
            if shopping_list_id and product_id:
                association = session.query(Association) \
                              .filter_by(Shoppinglist_ID=shopping_list_id,
                                         Product_ID=product_id).first()
                session.delete(association)
                session.commit()
            else:
                print("Either Shopping List or Product does not exist.")


if __name__ == '__main__':

    print(Functions.read_shopping_lists())
