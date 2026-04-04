import sqlite3
from database import db_core

def guardar_vehiculos(id_cliente, id_marca, id_modelo, placa, year, id_tipo, id_color):
    error= True
    try:
        conn= db_core.conectBaseDeDatos()
        query=conn.cursor()
        data="INSERT INTO VEHICULOS VALUES (Null,?,?,?,?,?,?,?,?)"
        values=(id_cliente, id_marca, id_modelo, placa, year, id_tipo, id_color,"activo")
        query.execute(data,values)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        conn.close()
        error=False
        print (e)
    return error

def mostrar_vehiculos_registrados():
    try: 
        conn= db_core.conectBaseDeDatos()
        query= conn.cursor()
        query.execute(
            '''SELECT
                V.id_vehiculo,
                V.id_cliente,
                MAR.MARCA,
                MOD.MODELO,
                V.PLACA,
                V.YEAR,
                TIP.TIPO,
                COL.COLOR,
                CLN.CEDULA,
                CLN.NOMBRES,
                CLN.APELLIDOS,
                CLN.TELEFONO
            FROM VEHICULOS V
            LEFT JOIN CLIENTES CLN ON V.id_cliente = CLN.id_cliente
            LEFT JOIN MARCAS_VEHICULOS MAR ON V.id_marca = MAR.id_marca
            LEFT JOIN MODELOS_VEHICULOS MOD ON V.id_modelo = MOD.id_modelo
            LEFT JOIN TIPOS_VEHICULOS TIP ON V.id_tipo = TIP.id_tipo
            LEFT JOIN COLORES COL ON V.id_color = COL.id_color
        
        ''')
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error:
        conn.close()
def editar_datos_vehiculo(id_cliente, id_marca, id_modelo, placa, year, id_tipo, id_color, id_vehiculo):
    error=True
    try:
        conn=db_core.conectBaseDeDatos()
        query=conn.cursor()
        edit="UPDATE VEHICULOS SET id_cliente=?, id_marca=?, id_modelo=?, PLACA=?, YEAR=?, id_tipo=?, id_color=? WHERE id_vehiculo=?"
        values=id_cliente, id_marca, id_modelo, placa, year, id_tipo, id_color, id_vehiculo
        query.execute(edit, values)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)
        conn.close()
        error=False
    return error
