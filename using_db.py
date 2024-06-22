import mysql.connector
import json
from file_manage import open_file_read, get_key

from cryptography.fernet import Fernet


def desencriptar(file_encriptados, clave):
    """
        Función utilizada para desencriptar los datos de la base de datos.

        Parámetros:
            -  file_encriptados: ruta del archivo donde se encuentran los datos encriptados.
            - clave: clave del archivo que contiene la info de la bd.
    """

    fernet = Fernet(clave)
    datos = open_file_read(file_encriptados)
    desencriptados = fernet.decrypt(datos)
    data = json.loads(desencriptados.decode())
    return data

def initialize_db():
    clave = get_key('./files/pass.key')
    datos_den = desencriptar('./files/db_info.json', clave)

    db = mysql.connector.connect(
         host=datos_den["host"],
         user=datos_den["user"],
         password=datos_den["password"],
         database= datos_den["database"]
     )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM Person")
    myresult = cursor.fetchall()

    print(myresult)
    

initialize_db()
