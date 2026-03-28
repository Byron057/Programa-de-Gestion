import sqlite3
from database import db_core

class catalogos_vehiculos():
    def mostrar_marcas():
        conn= db_core.conn_db.conectBaseDeDatos()
        
        query=conn.cursor()
        query.execute("SELECT * FROM MARCAS_VEHICULOS")