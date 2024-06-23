from file_manage import open_file_read
from cryptography.fernet import Fernet
import mysql.connector
import json


def data_handling():
    key = open_file_read("./files/pass.key")
    fernet = Fernet(key)
    encripted_data = open_file_read("./files/db_info.json")

    dencripted_data = fernet.decrypt(encripted_data)
    data = json.loads(dencripted_data.decode())
    return data


def create_db():
    db_data = data_handling()
    db = mysql.connector.connect(
        host=db_data["host"],
        user=db_data["user"],
        password=db_data["password"],
    )
    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS challenge")


def create_table():
    db_data = data_handling()
    db = mysql.connector.connect(
        host=db_data["host"],
        user=db_data["user"],
        password=db_data["password"],
        database='challenge',
    )

    mycursor = db.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS Files (file_id VARCHAR(255) PRIMARY KEY, title VARCHAR(100) NOT NULL, owner VARCHAR(50), modified_date DATETIME)"
    )
