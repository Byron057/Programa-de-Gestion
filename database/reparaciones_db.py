import sqlite3
from database import db_core

def guardar_repuestos_utilizados(id_orden_rep,id_repuesto, id_marca, id_proveedor):
    error=True
    try:
        conn=db_core.conectBaseDeDatos()
        query=conn.cursor()
        query.execute("INSERT INTO REPUESTOS_UTILIZADOS VALUES (Null,?,?, ?, ?)", (id_orden_rep,id_repuesto, id_marca, id_proveedor, ))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)
        conn.close()
        error=False
    return error
#editar y arreglar, variables mal puestas
def guardar_reparaciones_realizadas(id_orden_rep, reparacion,precio):
    error=True
    try:
        conn=db_core.conectBaseDeDatos()
        query=conn.cursor()
        query.execute("INSERT INTO REPARACIONES_REALIZADAS VALUES(Null,?,?,?)",(id_orden_rep, reparacion,precio,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)
        conn.close()
        error=False
    return error

def guardar_orden_reparacion(
    id_vehiculo, fecha_ingreso, fecha_salida, id_personal, precio_total, 
    kilometraje_actual, proximo_kilometraje):
    try:
        conn=db_core.conectBaseDeDatos()
        query=conn.cursor()
        query.execute("INSERT INTO ORDEN_REPARACION VALUES(NULL,?,?,?,?,?,?,?) ",
            (id_vehiculo,fecha_ingreso,fecha_salida,
            id_personal,precio_total,kilometraje_actual,proximo_kilometraje,)
        )
        conn.commit()
        conn.close()
        return query.lastrowid
    except sqlite3.Error as e:
        print(e)
        conn.close()
        
def guardar_rutas_imagenes_veh(id_orden_reparacion, ruta):
    try:
        conn=db_core.conectBaseDeDatos()
        query=conn.cursor()
        query.execute("INSERT INTO IMAGENES_VEHICULOS VALUES(NULL,?,?)", (id_orden_reparacion, ruta,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)
        conn.close()        
