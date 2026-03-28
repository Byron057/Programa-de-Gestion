# 🔧 Sistema de Gestión para Taller Automotriz

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Flet](https://img.shields.io/badge/Flet-UI-purple?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Estado-Desarrollo_Activo-success?style=for-the-badge)

¡Hola! Bienvenido al repositorio de mi primer proyecto de desarrollo de software a gran escala.

## 👋 Sobre mí
Soy **Byron Velastegui**, estudiante de Ingeniería de Software en la Universidad Técnica de Cotopaxi (UTC).

* 🐍 **Mi stack:** Python (Es mi primer lenguaje).
* ⏱️ **Experiencia:** Llevo aproximadamente **3 meses** aprendiendo programación.
* 🎯 **Objetivo Actual:** Consolidar mis conocimientos en interfaces gráficas modernas (Flet), arquitectura de software modular y bases de datos relacionales.

## 🚧 Estado del Proyecto
Este proyecto acaba de dar un salto de prototipo visual a la **fase de integración funcional**. Actualmente, estoy conectando la interfaz gráfica con el motor de base de datos y aplicando buenas prácticas de modularización.

**Lo que encontrarás en el código ahora mismo:**
* 🏗️ **Arquitectura Modular:** Separación clara entre vistas (`views`), controladores (`controls`), núcleo de base de datos (`db_core`) y componentes UI (`components`).
* 🔀 **Enrutamiento Dinámico:** Sistema de navegación (Router) implementado para cambiar fluidamente entre el Login y el Dashboard.
* 💾 **Base de Datos Autogestionada:** Creación dinámica de la base de datos SQLite y de los directorios locales (`assets/fotos_personal`) al arrancar el sistema por primera vez.
* ✨ **Experiencia de Usuario (UX):** Alertas asíncronas para el manejo de errores y éxitos.
* 🔒 **Seguridad Básica:** Uso de archivos `.env` y variables de entorno para proteger credenciales y rutas.

**Lo que falta (Próximos pasos):**
* [x] Diseñar el menú principal y configurar el enrutamiento.
* [x] Conectar la aplicación a una Base de Datos (SQLite).
* [ ] Finalizar y pulir las validaciones de los CRUDs (Clientes, Vehículos, etc.).
* [ ] Implementar la lógica completa de recuperación de contraseña vía Email (SMTP).
* [ ] Generar reportes y estadísticas en el Dashboard.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python
* **Frontend / Interfaz:** Flet (Basado en Flutter)
* **Base de Datos:** SQLite3
* **Gestión de Entorno:** `python-dotenv`

## 🤝 Llamado a la comunidad
Como estoy en pleno proceso de aprendizaje, este repositorio es mi "campo de entrenamiento" real. Ya he logrado superar la barrera del enrutamiento y la conexión a bases de datos, pero toda ayuda es bienvenida.

**Me ayudaría mucho recibir consejos sobre:**
1. ¿Cuáles son las mejores prácticas para manejar el estado global (como la sesión del usuario logueado) a través de múltiples vistas en Flet?
2. ¿Alguna recomendación para optimizar consultas relacionales en Python con SQLite cuando el volumen de datos empiece a crecer?
3. Consejos de seguridad adicionales para sistemas de escritorio que manejan datos de clientes.
4. Consejos sobre la Estructira del codigo

¡Gracias por visitar, leer mi código y apoyar mi camino en la ingeniería de software!

---
*Desarrollado por Byron Velastegui - Estudiante UTC.*