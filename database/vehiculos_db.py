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
    return error, query.lastrowid

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
                CLN.TELEFONO,
                
                O.id_orden_reparacion,
                O.FECHA_INGRESO,
                O.FECHA_SALIDA,
                P.id_personal,
                O.PRECIO_TOTAL,
                O.KILOMETRAJE_ACTUAL,
                O.KILOMETRAJE_PROXIMO,
                
                P.NOMBRES,
                P.APELLIDOS,
                P.CEDULA,
                
                RR.id_reparacion,
                RR.REPARACION,
                RR.PRECIO,
                
                RU.id_rep_uti,
                R.REPUESTO,
                MR.MARCA_REPUESTO,
                PR.PROVEEDOR,
                
                IV.id_imagen_vehiculo,
                IV.RUTA_IMAGEN
                
            FROM VEHICULOS V
            
            LEFT JOIN CLIENTES CLN ON V.id_cliente = CLN.id_cliente
            LEFT JOIN MARCAS_VEHICULOS MAR ON V.id_marca = MAR.id_marca
            LEFT JOIN MODELOS_VEHICULOS MOD ON V.id_modelo = MOD.id_modelo
            LEFT JOIN TIPOS_VEHICULOS TIP ON V.id_tipo = TIP.id_tipo
            LEFT JOIN COLORES COL ON V.id_color = COL.id_color
        
            LEFT JOIN ORDEN_REPARACION O ON V.id_vehiculo = O.id_vehiculo
            LEFT JOIN PERSONAL P ON O.id_personal = P.id_personal
            LEFT JOIN REPARACIONES_REALIZADAS RR ON O.id_orden_reparacion = RR.id_orden_reparacion
            LEFT JOIN REPUESTOS_UTILIZADOS RU ON O.id_orden_reparacion = RU.id_orden_reparacion
            LEFT JOIN REPUESTOS R ON RU.id_repuesto = R.id_repuesto
            LEFT JOIN MARCA_REPUESTOS MR ON RU.id_marca_repuesto = MR.id_marca_repuesto
            LEFT JOIN PROVEEDOR_REPUESTOS PR ON RU.id_proveedor = PR.id_proveedor
            LEFT JOIN IMAGENES_VEHICULOS IV ON O.id_orden_reparacion = IV.id_orden_reparacion
            
            WHERE V.ESTADO = "activo"
            
            ORDER BY
            V.id_vehiculo ASC,
            O.id_orden_reparacion DESC,
            RR.id_reparacion DESC
                    
        ''')
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error as e:
        print(e)
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
def eliminar_vehiculo(id):
    try: 
        conn= db_core.conectBaseDeDatos()
        query=conn.cursor()
        edit= "UPDATE VEHICULOS SET ESTADO='inactivo' WHERE id_vehiculo=?"
        value=(id,)
        query.execute(edit, value)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        conn.close()
        print(e)
def contar_vehiculos_activos():
    conn= db_core.conectBaseDeDatos()
    query=conn.cursor()
    query.execute('SELECT COUNT(*) FROM VEHICULOS WHERE ESTADO="activo"')
    total = query.fetchone()[0]
    conn.close()
    return total