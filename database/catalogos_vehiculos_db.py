import sqlite3
from database import db_core

def mostrar_marcas():
    try:
        conn= db_core.conectBaseDeDatos()
        
        query=conn.cursor()
        query.execute("SELECT * FROM MARCAS_VEHICULOS")
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error as e:
        conn.close()
        print(e)
def guardar_nueva_marca(marca):
    try:
        conn=db_core.conectBaseDeDatos()
        query= conn.cursor()
        query.execute('INSERT OR IGNORE INTO MARCAS_VEHICULOS  (MARCA) VALUES (?)', (marca,))
        query.execute("SELECT id_marca FROM MARCAS_VEHICULOS WHERE MARCA=?",(marca,))
        id_marca=query.fetchone()[0]
        conn.commit()
        conn.close()
        return id_marca
    except sqlite3.Error as e:
        conn.close()
        print(e)
def mostrar_modelos(id):
    try:
        conn= db_core.conectBaseDeDatos()
        query= conn.cursor()
        query.execute('SELECT id_modelo,MODELO FROM MODELOS_VEHICULOS WHERE id_marca=? ',(id,))
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error as e:
        conn.close()
        print(e)
def guardar_nuevo_modelo(id_marca,modelo):
    try:
        conn=db_core.conectBaseDeDatos()
        query= conn.cursor()
        query.execute('INSERT OR IGNORE INTO MODELOS_VEHICULOS (id_marca,MODELO) VALUES (?,?)', (id_marca,modelo,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        conn.close()
        print(e)
def mostrar_colores():
    try:
        conn= db_core.conectBaseDeDatos()
        query= conn.cursor()
        query.execute('SELECT * FROM COLORES')
        resultado=query.fetchall()
        conn.close()
        return resultado
    except sqlite3 as e:
        conn.close()
        print(e)
def guardar_nuevo_color(color):
    try:
        conn=db_core.conectBaseDeDatos()
        query= conn.cursor()
        query.execute('INSERT OR IGNORE INTO COLORES (COLOR) VALUES (?)', (color,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        conn.close()
        print(e)
def mostrar_tipos_vehiculos():
    try: 
        conn= db_core.conectBaseDeDatos()
        query= conn.cursor()
        query.execute("SELECT * FROM TIPOS_VEHICULOS")
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error as e:
        conn.close()
        print(e)
def guardar_nuevo_tipo(tipo):
    try:
        conn=db_core.conectBaseDeDatos()
        query= conn.cursor()
        query.execute('INSERT OR IGNORE INTO TIPOS_VEHICULOS (TIPO) VALUES (?)', (tipo,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        conn.close()
        print(e)