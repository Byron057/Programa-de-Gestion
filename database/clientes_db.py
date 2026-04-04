import sqlite3
from database import db_core


def guardar_clientes(cedula, nombres, apellidos,telefono, correo, provincia, ciudad, direccion ):
    error= True
    ultimo_id=None
    try:
        conn=db_core.conectBaseDeDatos()
        query= conn.cursor()
        
        data='INSERT INTO CLIENTES VALUES (Null,?,?,?,?,?,?,?,?,?)'
        values=(cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,'activo')
        query.execute(data,values)
        ultimo_id=query.lastrowid
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)
        conn.close()
        error= False
    return error,ultimo_id

def mostrar_clientes_registrados():
    try: 
        conn= db_core.conectBaseDeDatos()
        query= conn.cursor()
        query.execute('''
            SELECT 
                C.id_cliente,
                C.CEDULA,
                C.NOMBRES,
                C.APELLIDOS,
                C.TELEFONO,
                C.CORREO,
                C.PROVINCIA,
                C.CIUDAD,
                C.DIRECCION,
                
                V.id_vehiculo,
                V.PLACA,
                MOD.MODELO,
                TIP.TIPO
                
            FROM CLIENTES C
            LEFT JOIN VEHICULOS V ON C.id_cliente = V.id_cliente
            LEFT JOIN MODELOS_VEHICULOS MOD ON V.id_modelo = MOD.id_modelo
            LEFT JOIN TIPOS_VEHICULOS TIP ON V.id_tipo = TIP.id_tipo
            WHERE C.ESTADO = "activo"
            ORDER BY C.APELLIDOS ASC;
        ''')
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error as e:
        print(e)
        conn.close()
        return []

def editar_datos_clientes(cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,id):
    error=True
    try:
        conn= db_core.conectBaseDeDatos()
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

def eliminar_clientes(id):
    try: 
        conn= db_core.conectBaseDeDatos()
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
    conn= db_core.conectBaseDeDatos()
    query=conn.cursor()
    query.execute('SELECT COUNT(*) FROM CLIENTES WHERE ESTADO="activo"')
    total = query.fetchone()[0]
    conn.close()
    return total