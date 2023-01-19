import sqlalchemy
from datamodel import Base  #, shopping_list, product


def connect_database():
    db_connection = sqlalchemy.create_engine("sqlite:///D:\\leina\\Documents\\Schule\\Softwareentwicklung (SEW)\\sew_einkaufsliste-1\\Shopping List\\database.sql")
    Base.metadata.create_all(db_connection)
    session_factory = sqlalchemy.orm.sessionmaker()
    session_factory.configure(bind=db_connection)


connect_database()
