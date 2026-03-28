import sqlite3
from database import db_core

class cliente_table():
    
    def guardar_clientes(self, cedula, nombres, apellidos,telefono, correo, provincia, ciudad, direccion ):
        error= True
        try:
            conn=db_core.conn_db.conectBaseDeDatos()
            query= conn.cursor()
            
            data='INSERT INTO CLIENTES VALUES (Null,?,?,?,?,?,?,?,?,?)'
            values=(cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,'activo')
            
            query.execute(data,values)
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(e)
            conn.close()
            error= False
        return error
    
    def mostrar_clientes_registrados():
        try: 
            conn= db_core.conn_db.conectBaseDeDatos()
            query= conn.cursor()
            query.execute('SELECT * FROM CLIENTES WHERE ESTADO="activo" ORDER BY APELLIDOS ASC; ')
            resultado= query.fetchall()
            conn.close()
            return resultado
        except sqlite3.Error:
            conn.close()
    
    def editar_datos_clientes(self,cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,id):
        error=True
        try:
            conn= db_core.conn_db.conectBaseDeDatos()
            query=conn.cursor()
            edit= "UPDATE CLIENTES SET CEDULA=?, NOMBRES=?, APELLIDOS=?, TELEFONO=?, CORREO=?, PROVINCIA=?, CIUDAD=?, DIRECCION=? WHERE id_cliente=?"
            values=(cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,id)
            query.execute(edit,values)
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            error=False
            print(e)
            conn.close()
        return error
    def obtener_por_id(self,id):
        try:
            conn=db_core.conn_db.conectBaseDeDatos()
            query=conn.cursor()
            query.execute('SELECT * FROM CLIENTES WHERE id_cliente=?', (id,))
            data=query.fetchone()
            conn.close()
            return data
        except sqlite3.Error as e:
            conn.close()
            print(e)
    
    def eliminar_clientes(id):
        try: 
            conn= db_core.conn_db.conectBaseDeDatos()
            query=conn.cursor()
            edit= "UPDATE CLIENTES SET ESTADO='inactivo' WHERE id_cliente=?"
            value=(id,)
            query.execute(edit, value)
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            conn.close()
            print(e)
    def contar_clientes_activos():
        conn= db_core.conn_db.conectBaseDeDatos()
        query=conn.cursor()
        query.execute('SELECT COUNT(*) FROM CLIENTES WHERE ESTADO="activo"')
        total = query.fetchone()[0]
        conn.close()
        return total