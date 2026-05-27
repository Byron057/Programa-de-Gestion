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
        query.execute("SELECT id_marca FROM MARCAS_VEHICULOS WHERE MARCA=?",(marca,))
        id_marca=query.fetchone()
        if id_marca:
            return id_marca[0]
        query.execute('INSERT OR IGNORE INTO MARCAS_VEHICULOS  (MARCA) VALUES (?)', (marca,))
        
        conn.commit()
        conn.close()
        return query.lastrowid

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
        query.execute("SELECT id_modelo FROM MODELOS_VEHICULOS WHERE MODELO  =?",(modelo,))
        verificacion=query.fetchone()
        if not verificacion:
            query.execute('INSERT INTO MODELOS_VEHICULOS (id_marca,MODELO) VALUES (?,?)', (id_marca,modelo,))
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
        query.execute("SELECT id_color FROM COLORES WHERE COLOR=?", (color,))
        verificacion=query.fetchone()
        if not verificacion:
            query.execute('INSERT INTO COLORES (COLOR) VALUES (?)', (color,))
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
        query.execute("SELECT id_tipo FROM TIPOS_VEHICULOS WHERE TIPO=?", (tipo,))
        verificacion=query.fetchone()
        if not verificacion:
            query.execute('INSERT OR IGNORE INTO TIPOS_VEHICULOS (TIPO) VALUES (?)', (tipo,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        conn.close()
        print(e)
        
def guardar_repuesto(repuesto): 
    try:
        conn=db_core.conectBaseDeDatos()
        query=conn.cursor()
        query.execute("SELECT id_repuesto FROM REPUESTOS WHERE REPUESTO=? ", (repuesto,))
        id_repuesto=query.fetchone()
        if id_repuesto:
            return id_repuesto[0]
        query.execute("INSERT INTO REPUESTOS (REPUESTO) VALUES (?)", (repuesto,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)
        conn.close()
    return query.lastrowid
        
def guardar_marca_repuesto(marca_repuesto):
    try:
        conn=db_core.conectBaseDeDatos()
        query=conn.cursor()
        query.execute("SELECT id_marca_repuesto FROM MARCA_REPUESTOS WHERE MARCA_REPUESTO=? ", (marca_repuesto,))
        id_marca=query.fetchone()
        if id_marca:
            return id_marca[0]
        query.execute("INSERT INTO MARCA_REPUESTOS (MARCA_REPUESTO) VALUES (?)", (marca_repuesto,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)
        conn.close()
    return query.lastrowid
        
def guardar_proveedor_repuesto(proveedor_repuesto):
    try:
        conn=db_core.conectBaseDeDatos()
        query=conn.cursor()
        query.execute("SELECT id_proveedor FROM PROVEEDOR_REPUESTOS WHERE PROVEEDOR=?",(proveedor_repuesto,))
        id_proveedor= query.fetchone()
        if id_proveedor:
            return id_proveedor[0]
        query.execute("INSERT INTO PROVEEDOR_REPUESTOS (PROVEEDOR) VALUES (?)", (proveedor_repuesto,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)
        conn.close()
    return query.lastrowid

def mostrar_repuestos():
    try: 
        conn=db_core.conectBaseDeDatos()
        query=conn.cursor()
        query.execute("SELECT * FROM REPUESTOS")
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error as e:
        print(e)
        conn.close()
def mostrar_marca_repuestos():
    try: 
        conn=db_core.conectBaseDeDatos()
        query=conn.cursor()
        query.execute("SELECT * FROM MARCA_REPUESTOS")
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error as e:
        print(e)
        conn.close()
def mostrar_proveedor_repuestos():
    try: 
        conn=db_core.conectBaseDeDatos()
        query=conn.cursor()
        query.execute("SELECT * FROM PROVEEDOR_REPUESTOS")
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error as e:
        print(e)
        conn.close()
