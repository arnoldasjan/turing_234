import psycopg2
import os


def connect_to_database():
    db_connection = psycopg2.connect(
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST'],
        port="5432"
    )

    db_connection.autocommit = True
    return db_connection
