import sqlite3
import json 
import os
from config import *


def conectBaseDeDatos():
    try:
        conn= sqlite3.connect(RUTA_DB)
        return conn
    except sqlite3.Error as error:
        print(error)
        return None
    
def tabla_vacia(query, tabla):
    query.execute(f"SELECT COUNT(*) FROM {tabla}")
    return query.fetchone()[0]==0
def data_necesaria(db_path=RUTA_DB):
    try:
        conn=sqlite3.connect(db_path)
        query=conn.cursor()
        query.execute("PRAGMA foreign_keys = ON")
        query.execute("""
            CREATE TABLE IF NOT EXISTS PROVINCIAS (
                id_prov INTEGER PRIMARY KEY AUTOINCREMENT,
                PROVINCIA TEXT UNIQUE NOT NULL
            )"""
        )
        if tabla_vacia(query,"PROVINCIAS"):

            query.executescript("""INSERT OR IGNORE INTO PROVINCIAS (PROVINCIA) VALUES 
            ('Azuay'), ('Bolívar'), ('Cañar'), ('Carchi'), ('Chimborazo'),
            ('Cotopaxi'), ('El Oro'), ('Esmeraldas'), ('Galápagos'), ('Guayas'),
            ('Imbabura'), ('Loja'), ('Los Ríos'), ('Manabí'), ('Morona Santiago'),
            ('Napo'), ('Orellana'), ('Pastaza'), ('Pichincha'), ('Santa Elena'),
            ('Santo Domingo de los Tsáchilas'), ('Sucumbíos'), ('Tungurahua'),
            ('Zamora Chinchipe');
        """)
        query.executescript("""
            CREATE TABLE IF NOT EXISTS CIUDADES(
                id_ciudad INTEGER PRIMARY KEY AUTOINCREMENT,
                CIUDAD TEXT,
                id_prov INTEGER,
                UNIQUE(CIUDAD, id_prov),
                FOREIGN KEY (id_prov) REFERENCES PROVINCIAS (id_prov)
            )"""
        )
        if tabla_vacia(query,"CIUDADES"):
            query.execute("""INSERT OR IGNORE INTO CIUDADES (CIUDAD, id_prov) VALUES 
                ('Cuenca', 1), ('Camilo Ponce Enríquez', 1), ('Chordeleg', 1), ('El Pan', 1), ('Girón', 1), ('Guachapala', 1), ('Gualaceo', 1), ('Nabón', 1), ('Oña', 1), ('Paute', 1), ('Pucará', 1), ('San Fernando', 1), ('Santa Isabel', 1), ('Sevilla de Oro', 1), ('Sigsig', 1),
                ('Guaranda', 2), ('Caluma', 2), ('Chillanes', 2), ('Chimbo', 2), ('Echeandía', 2), ('Las Naves', 2), ('San Miguel', 2),
                ('Azogues', 3), ('Biblián', 3), ('Cañar', 3), ('Déleg', 3), ('El Tambo', 3), ('La Troncal', 3), ('Suscal', 3),
                ('Tulcán', 4), ('Bolívar', 4), ('Espejo', 4), ('Mira', 4), ('Montúfar', 4), ('San Pedro de Huaca', 4),
                ('Riobamba', 5), ('Alausí', 5), ('Chambo', 5), ('Chunchi', 5), ('Colta', 5), ('Cumandá', 5), ('Guamote', 5), ('Guano', 5), ('Pallatanga', 5), ('Penipe', 5),
                ('Latacunga', 6), ('La Maná', 6), ('Pangua', 6), ('Pujilí', 6), ('Salcedo', 6), ('Saquisilí', 6), ('Sigchos', 6),
                ('Machala', 7), ('Arenillas', 7), ('Atahualpa', 7), ('Balsas', 7), ('Chilla', 7), ('El Guabo', 7), ('Huaquillas', 7), ('Las Lajas', 7), ('Marcabelí', 7), ('Pasaje', 7), ('Piñas', 7), ('Portovelo', 7), ('Santa Rosa', 7), ('Zaruma', 7),
                ('Esmeraldas', 8), ('Atacames', 8), ('Eloy Alfaro', 8), ('Muisne', 8), ('Quinindé', 8), ('Río Verde', 8), ('San Lorenzo', 8),
                ('San Cristóbal', 9), ('Isabela', 9), ('Santa Cruz', 9),
                ('Guayaquil', 10), ('Alfredo Baquerizo Moreno (Juján)', 10), ('Balao', 10), ('Balzar', 10), ('Colimes', 10), ('Daule', 10), ('Durán', 10), ('El Empalme', 10), ('El Triunfo', 10), ('General Antonio Elizalde (Bucay)', 10), ('Isidro Ayora', 10), ('Lomas de Sargentillo', 10), ('Marcelino Maridueña', 10), ('Milagro', 10), ('Naranjal', 10), ('Naranjito', 10), ('Nobol', 10), ('Palestina', 10), ('Pedro Carbo', 10), ('Playas', 10), ('Salitre', 10), ('Samborondón', 10), ('Santa Lucía', 10), ('Simón Bolívar', 10), ('Yaguachi', 10),
                ('Ibarra', 11), ('Antonio Ante', 11), ('Cotacachi', 11), ('Otavalo', 11), ('Pimampiro', 11), ('San Miguel de Urcuquí', 11),
                ('Loja', 12), ('Calvas', 12), ('Catamayo', 12), ('Celica', 12), ('Chaguarpamba', 12), ('Espíndola', 12), ('Gonzanamá', 12), ('Macará', 12), ('Olmedo', 12), ('Paltas', 12), ('Pindal', 12), ('Puyango', 12), ('Quilanga', 12), ('Saraguro', 12), ('Sozoranga', 12), ('Zapotillo', 12),
                ('Babahoyo', 13), ('Baba', 13), ('Buena Fe', 13), ('Mocache', 13), ('Montalvo', 13), ('Palenque', 13), ('Puebloviejo', 13), ('Quevedo', 13), ('Quinsaloma', 13), ('Urdaneta', 13), ('Valencia', 13), ('Ventanas', 13), ('Vinces', 13),
                ('Portoviejo', 14), ('24 de Mayo', 14), ('Bolívar', 14), ('Chone', 14), ('El Carmen', 14), ('Flavio Alfaro', 14), ('Jama', 14), ('Jaramijó', 14), ('Jipijapa', 14), ('Junín', 14), ('Manta', 14), ('Montecristi', 14), ('Olmedo', 14), ('Paján', 14), ('Pedernales', 14), ('Pichincha', 14), ('Puerto López', 14), ('Rocafuerte', 14), ('San Vicente', 14), ('Santa Ana', 14), ('Sucre', 14), ('Tosagua', 14),
                ('Morona', 15), ('Gualaquiza', 15), ('Huamboya', 15), ('Limón Indanza', 15), ('Logroño', 15), ('Pablo Sexto', 15), ('Palora', 15), ('Santiago', 15), ('San Juan Bosco', 15), ('Sucúa', 15), ('Taisha', 15), ('Tiwintza', 15),
                ('Tena', 16), ('Archidona', 16), ('Carlos Julio Arosemena Tola', 16), ('Quijos', 16), ('El Chaco', 16),
                ('Orellana', 17), ('Aguuarico', 17), ('La Joya de los Sachas', 17), ('Loreto', 17),
                ('Pastaza', 18), ('Mera', 18), ('Santa Clara', 18), ('Arajuno', 18),
                ('Quito', 19), ('Cayambe', 19), ('Mejía', 19), ('Pedro Moncayo', 19), ('Pedro Vicente Maldonado', 19), ('Puerto Quito', 19), ('Rumiñahui', 19), ('San Miguel de los Bancos', 19),
                ('Santa Elena', 20), ('La Libertad', 20), ('Salinas', 20),
                ('Santo Domingo', 21), ('La Concordia', 21),
                ('Lago Agrio', 22), ('Cascales', 22), ('Cuyabeno', 22), ('Gonzalo Pizarro', 22), ('Putumayo', 22), ('Shushufindi', 22), ('Sucumbíos', 22),
                ('Ambato', 23), ('Baños de Agua Santa', 23), ('Cevallos', 23), ('Mocha', 23), ('Patate', 23), ('Quero', 23), ('San Pedro de Pelileo', 23), ('Santiago de Píllaro', 23), ('Tisaleo', 23),
                ('Zamora', 24), ('Centinela del Cóndor', 24), ('Chinchipe', 24), ('El Pangui', 24), ('Nangaritza', 24), ('Palanda', 24), ('Paquisha', 24), ('Yacuambi', 24), ('Yantzaza', 24);
                """)
        
        query.execute("""
            CREATE TABLE IF NOT EXISTS PERSONAL(
                id_personal INTEGER PRIMARY KEY AUTOINCREMENT,
                CEDULA TEXT UNIQUE,
                NOMBRES TEXT,
                APELLIDOS TEXT,
                TELEFONO TEXT,
                CORREO TEXT,
                PROVINCIA TEXT, 
                CIUDAD TEXT,
                DIRECCION TEXT,
                FOTO TEXT,
                ESTADO TEXT DEFAULT 'activo' CHECK("ESTADO" IN ('activo', 'inactivo'))
                
            )     
        """)
        
        query.execute("""
            CREATE TABLE IF NOT EXISTS CLIENTES(
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                CEDULA TEXT UNIQUE,
                NOMBRES TEXT,
                APELLIDOS TEXT,
                TELEFONO TEXT,
                CORREO TEXT,
                PROVINCIA TEXT, 
                CIUDAD TEXT,
                DIRECCION TEXT,
                ESTADO TEXT DEFAULT 'activo' CHECK("ESTADO" IN ('activo', 'inactivo'))
            )     
        """)
        query.execute("""
            CREATE TABLE IF NOT EXISTS MARCAS_VEHICULOS(
                id_marca INTEGER PRIMARY KEY AUTOINCREMENT,
                MARCA TEXT UNIQUE
            );
        """)

        if tabla_vacia(query, "MARCAS_VEHICULOS"):
            query.executescript("""
                INSERT INTO MARCAS_VEHICULOS (MARCA) VALUES
                ('Toyota'), ('Chevrolet'), ('Nissan'), ('Kia'), ('Hyundai');
            """)
        query.execute("""
            CREATE TABLE IF NOT EXISTS MODELOS_VEHICULOS(
                id_modelo INTEGER PRIMARY KEY AUTOINCREMENT,
                id_marca INTEGER,
                MODELO TEXT,
                UNIQUE(id_marca, MODELO),
                FOREIGN KEY (id_marca) REFERENCES MARCAS_VEHICULOS (id_marca)
            );
        """)

        if tabla_vacia(query, "MODELOS_VEHICULOS"):
            query.executescript("""
                INSERT INTO MODELOS_VEHICULOS (id_marca, MODELO) VALUES
                (1, 'Hilux'), (1, 'Corolla'), (1, 'Yaris'),
                (2, 'Sail'), (2, 'D-Max'), (2, 'Spark'),
                (3, 'Frontier'), (3, 'Versa'), (3, 'Sentra');
            """)
        
        query.execute("""
            CREATE TABLE IF NOT EXISTS COLORES(
                id_color INTEGER PRIMARY KEY AUTOINCREMENT,
                COLOR TEXT UNIQUE
            );
        """)

        if tabla_vacia(query, "COLORES"):
            query.executescript("""
                INSERT INTO COLORES (COLOR) VALUES
                ('Negro'), ('Blanco'), ('Gris'), ('Rojo'), ('Azul'),
                ('Plata'), ('Verde');
            """)
        query.execute("""
            CREATE TABLE IF NOT EXISTS TIPOS_VEHICULOS(
                id_tipo INTEGER PRIMARY KEY AUTOINCREMENT,
                TIPO TEXT UNIQUE
            );
        """)

        if tabla_vacia(query, "TIPOS_VEHICULOS"):
            query.executescript("""
                INSERT INTO TIPOS_VEHICULOS (TIPO) VALUES
                ('Automovil'), ('Camioneta'), ('Furgoneta'), ('Taxi');
            """)
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS VEHICULOS(
                id_vehiculo INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER,
                id_marca INTEGER,
                id_modelo INTEGER,
                PLACA TEXT UNIQUE,
                YEAR TEXT,
                id_tipo INTEGER,
                id_color INTEGER,
                ESTADO TEXT DEFAULT 'activo' CHECK("ESTADO" IN ('activo', 'inactivo')),
                
                FOREIGN KEY (id_cliente) REFERENCES CLIENTES (id_cliente),
                FOREIGN KEY (id_marca) REFERENCES MARCAS_VEHICULOS (id_marca),
                FOREIGN KEY (id_modelo) REFERENCES MODELOS_VEHICULOS (id_modelo),
                FOREIGN KEY (id_tipo) REFERENCES TIPOS_VEHICULOS (id_tipo),
                FOREIGN KEY (id_color) REFERENCES COLORES (id_color)
            )
        """)
        query.execute("""
             CREATE TABLE IF NOT EXISTS ORDEN_REPARACION(
                id_orden_reparacion INTEGER PRIMARY KEY AUTOINCREMENT,
                id_vehiculo INTEGER,
                FECHA_INGRESO TEXT,
                FECHA_SALIDA TEXT,
                id_personal INTEGER,
                PRECIO_TOTAL TEXT,
                KILOMETRAJE_ACTUAL TEXT,
                KILOMETRAJE_PROXIMO TEXT,
                
                FOREIGN KEY (id_vehiculo) REFERENCES VEHICULOS (id_vehiculo),   
                FOREIGN KEY (id_personal) REFERENCES PERSONAL (id_personal)   
             )
            
        """)
        
        query.execute("""
            CREATE TABLE IF NOT EXISTS REPUESTOS(
                id_repuesto INTEGER PRIMARY KEY AUTOINCREMENT,
                REPUESTO TEXT UNIQUE      
            )
        """)
        
        query.execute("""
            CREATE TABLE IF NOT EXISTS MARCA_REPUESTOS(
                id_marca_repuesto INTEGER PRIMARY KEY AUTOINCREMENT,
                MARCA_REPUESTO TEXT UNIQUE
                    
            )
        """)
        
        query.execute("""
            CREATE TABLE IF NOT EXISTS PROVEEDOR_REPUESTOS(
                id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
                PROVEEDOR TEXT UNIQUE
            )
        """)
        
        query.execute("""
            CREATE TABLE IF NOT EXISTS REPUESTOS_UTILIZADOS(
                id_rep_uti INTEGER PRIMARY KEY AUTOINCREMENT,
                id_orden_reparacion INTEGER,
                id_repuesto INTEGER,
                id_marca_repuesto INTEGER,
                id_proveedor INTEGER,
                
                FOREIGN KEY (id_orden_reparacion) REFERENCES ORDEN_REPARACION (id_orden_reparacion),
                FOREIGN KEY (id_repuesto) REFERENCES REPUESTOS (id_repuesto),
                FOREIGN KEY (id_marca_repuesto) REFERENCES MARCA_REPUESTOS (id_marca_repuesto),
                FOREIGN KEY (id_proveedor) REFERENCES PROVEEDOR_REPUESTOS (id_proveedor)
            )"""
        )
        query.execute("""
            CREATE TABLE IF NOT EXISTS REPARACIONES_REALIZADAS(
                id_reparacion INTEGER PRIMARY KEY AUTOINCREMENT,
                id_orden_reparacion INTEGER,
                REPARACION TEXT,
                PRECIO TEXT,
            
                FOREIGN KEY (id_orden_reparacion) REFERENCES ORDEN_REPARACION (id_orden_reparacion)
            )
        """            
        )
        query.execute("""
                    CREATE TABLE IF NOT EXISTS IMAGENES_VEHICULOS(
                        id_imagen_vehiculo INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_orden_reparacion INTEGER,
                        RUTA_IMAGEN TEXT,
                        
                        FOREIGN KEY (id_orden_reparacion) REFERENCES ORDEN_REPARACION (id_orden_reparacion)
                    )
                      
        """)
        query.execute("""
            CREATE TABLE IF NOT EXISTS USUARIOS(
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO TEXT,
                APELLIDO_USUARIO TEXT,
                CORREO TEXT,
                CONTRASEÑA TEXT,
                TELEFONO TEXT
            )
        """)
        if tabla_vacia(query, "TIPOS_VEHICULOS"):
            query.executescript("""
              INSERT INTO USUARIOS(id_usuario,NOMBRE_USUARIO, APELLIDO_USUARIO, CORREO, CONTRASEÑA, TELEFONO) VALUES
            (1, "MECASOFT", null, "MECASOFT2026", "MECASOFT2026", null);
            """)
     
        
        
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print(error)

def cargar_catalogo_provincias():
    try:
        conn= sqlite3.connect(RUTA_DB)
        query= conn.cursor()
        query.execute('SELECT * FROM PROVINCIAS;')
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error as errorw:
        conn.close()
        print(errorw)

def cargar_catalogo_ciudades(id_prov):
    try:
        conn= sqlite3.connect(RUTA_DB)
        query= conn.cursor()
        query.execute('SELECT id_ciudad, CIUDAD FROM CIUDADES WHERE id_prov=?', (id_prov,))
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error as error:
        conn.close()
        print(error)
def datos_login():
    try:
        conn = sqlite3.connect(RUTA_DB)
        query= conn.cursor()
        query.execute('SELECT * FROM USUARIOS WHERE id_usuario=1')
        resultado= query.fetchall()
        conn.close()
        return resultado
    except sqlite3.Error as error:
        conn.close()
        print(error)
        
def obtener_actividad_reciente():
    # 1. Usar la ruta correcta del archivo de configuración
    conexion = sqlite3.connect(RUTA_DB) 
    cursor = conexion.cursor()
    resultados = []

    try:
        # 2. Último Cliente (Se concatena NOMBRES y APELLIDOS. Se omite fecha porque no existe en la BD)
        cursor.execute("""
            SELECT 'Nuevo Cliente', NOMBRES || ' ' || APELLIDOS, CEDULA 
            FROM CLIENTES 
            ORDER BY id_cliente DESC LIMIT 1
        """)
        ultimo_cliente = cursor.fetchone() 
        if ultimo_cliente:
            resultados.append(ultimo_cliente)

        # 3. Último Vehículo (Se usa id_vehiculo)
        cursor.execute("""
            SELECT 'Nuevo Vehículo', M.MODELO, V.PLACA 
            FROM VEHICULOS V
            INNER JOIN MODELOS_VEHICULOS M ON V.id_modelo = M.id_modelo
            ORDER BY V.id_vehiculo DESC LIMIT 1
        """)
        ultimo_vehiculo = cursor.fetchone()
        if ultimo_vehiculo:
            resultados.append(ultimo_vehiculo)

        # 4. Última Reparación (Uniendo REPARACIONES_REALIZADAS con ORDEN_REPARACION para sacar la fecha)
        cursor.execute("""
            SELECT 'Nueva Reparación', R.REPARACION, V.PLACA 
            FROM REPARACIONES_REALIZADAS R
            INNER JOIN ORDEN_REPARACION O ON R.id_orden_reparacion = O.id_orden_reparacion
            INNER JOIN VEHICULOS V ON O.id_vehiculo = V.id_vehiculo
            ORDER BY R.id_reparacion DESC LIMIT 1
        """)
        ultima_reparacion = cursor.fetchone()
        if ultima_reparacion:
            resultados.append(ultima_reparacion)

        return resultados 

    except sqlite3.Error as e:
        print(f"Error de SQLite: {e}")
        conexion.close()
        return []