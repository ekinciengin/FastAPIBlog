from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db_sqlite():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_db_postgresql():

    connection = None
    try:
        connection = psycopg2.connect(
            host="database-1.c9aweaexlowz.eu-west-2.rds.amazonaws.com",
            port="5432",
            database="AudioLifeTest",
            user="postgres",
            password="Welcome1245")

        # create a cursor
        cur = connection.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')
