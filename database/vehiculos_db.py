import sqlite3
from database import db_core

class catalogos_vehiculos():
    def mostrar_marcas():
        try:
            conn= db_core.conn_db.conectBaseDeDatos()
            
            query=conn.cursor()
            query.execute("SELECT * FROM MARCAS_VEHICULOS")
            resultado= query.fetchall()
            conn.close()
            return resultado
        except sqlite3.Error as e:
            conn.close()
            print(e)
    def mostrar_modelos():
        try:
            conn= db_core.conn_db.conectBaseDeDatos()
            query= conn.cursor()
            query.execute('SELECT id_modelo, MODELO, ')
        except sqlite3.Error as e:
            conn.close()
            print(e)