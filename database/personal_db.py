import sqlite3
from database import db_core

class personal_table():
    def guardar_personal(self,cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,foto):
        error= True
        try:
            conn= db_core.conn_db.conectBaseDeDatos()
            query= conn.cursor()
            
            data='INSERT INTO PERSONAL VALUES (Null,?,?,?,?,?,?,?,?,?,?)'
            
            values=(cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,foto, 'activo')

            query.execute(data, values)
            conn.commit()
            
            conn.close()
            
        except sqlite3.Error as e:
            print(e)
            conn.close()
            error=False
        
        return error
    
    def mostrar_personal_registrado():
        try:
            conn= db_core.conn_db.conectBaseDeDatos()
            query= conn.cursor()
            query.execute("SELECT * FROM PERSONAL WHERE ESTADO ='activo';")
            resultado= query.fetchall()
            conn.close()
            return resultado
        except sqlite3.Error:
            conn.close()
            
    def editar_datos_personal(self,cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,foto,id):
        error= True
        try:
            conn= db_core.conn_db.conectBaseDeDatos()
            query= conn.cursor()
            edit= "UPDATE PERSONAL SET CEDULA=?, NOMBRES=?, APELLIDOS=?, TELEFONO=?, CORREO=?, PROVINCIA=?, CIUDAD=?, DIRECCION=?, FOTO=? WHERE id_personal=?"
            values=(cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,foto,id)
            query.execute(edit, values)
            conn.commit()
            conn.close()
            
        except sqlite3.Error as errore:
            conn.close()
            error=False
            print(errore)
        return error
    
    def obtener_por_id(self, id):
        conn = db_core.conn_db.conectBaseDeDatos()
        query = conn.cursor()
        query.execute("SELECT * FROM PERSONAL WHERE id_personal=?", (id,))
        data = query.fetchone()
        conn.close()
        return data
    
    def eliminar_datos_personal(id):
        try:
            conn= db_core.conn_db.conectBaseDeDatos()
            query= conn.cursor()
            edit= "UPDATE PERSONAL SET ESTADO='inactivo' WHERE id_personal=?"
            values=(id,)
            query.execute(edit, values)
            conn.commit()
            conn.close()
            
        except sqlite3.Error as error:
            conn.close()
            print(error)
    