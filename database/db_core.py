import sqlite3
import json 
import os

class conn_db():
    def conectBaseDeDatos():
        try:
            conn= sqlite3.connect("gestion_mecanica.db")
            print("coneccion exitosa")
            
            return conn
        except sqlite3.Error as error:
            print(error)
            return None
    def data_necesaria(db_path='gestion_mecanica.db'):
        try:
            conn=sqlite3.connect(db_path)
            query=conn.cursor()
            query.execute("PRAGMA foreign_keys = ON")
            query.executescript("""
                CREATE TABLE IF NOT EXISTS PROVINCIAS (
                    id_prov INTEGER PRIMARY KEY AUTOINCREMENT,
                    PROVINCIA TEXT UNIQUE NOT NULL
                );

                INSERT OR IGNORE INTO PROVINCIAS (PROVINCIA) VALUES 
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
                );
                
                INSERT OR IGNORE INTO CIUDADES (CIUDAD, id_prov) VALUES 
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
            query.executescript("""
                CREATE TABLE IF NOT EXISTS MARCAS_VEHICULOS(
                    id_marca INTEGER PRIMARY KEY AUTOINCREMENT,
                    MARCA TEXT UNIQUE
                );
                
                INSERT OR IGNORE INTO MARCAS_VEHICULOS (MARCA) VALUES
                ('Toyota'),('Chevrolet'),('Nissan'),('Kia'),('Hyundai');
                
                
            """)
            query.executescript("""
                CREATE TABLE IF NOT EXISTS MODELOS_VEHICULOS(
                    id_modelo INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_marca INTEGER,
                    MODELO TEXT UNIQUE,
                    FOREIGN KEY (id_marca) REFERENCES MARCAS_VEHICULOS (id_marca)
                );
                INSERT OR IGNORE INTO MODELOS_VEHICULOS (id_marca, MODELO) VALUES
                    (1, 'Hilux'), (1, 'Corolla'), (1, 'Yaris'), (1, 'Fortuner'), (1, 'RAV4'), 
                    (2, 'Sail'), (2, 'D-Max'), (2, 'Spark'), (2, 'Tracker'), (2, 'Aveo'), 
                    (3, 'Frontier'), (3, 'Versa'), (3, 'Sentra'), (3, 'Kicks'), (3, 'X-Trail');
            """)
            
            query.execute("""
                CREATE TABLE IF NOT EXISTS COLORES(
                    id_color INTEGER PRIMARY KEY AUTOINCREMENT,
                    COLOR TEXT UNIQUE
                )
            """)
            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            print(error)
    
    def cargar_catalogo_provincias():
        try:
            conn= sqlite3.connect("gestion_mecanica.db")
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
            conn= sqlite3.connect("gestion_mecanica.db")
            query= conn.cursor()
            query.execute('SELECT id_ciudad, CIUDAD FROM CIUDADES WHERE id_prov=?', (id_prov,))
            resultado= query.fetchall()
            conn.close()
            return resultado
        except sqlite3.Error as errorw:
            conn.close()
            print(errorw)