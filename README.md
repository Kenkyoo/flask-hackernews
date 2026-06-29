🚀 Flask HackerNews Clone (HTMX + Bootstrap 5)

¡Bienvenido al clon moderno de HackerNews! Este proyecto es una aplicación web ligera y altamente responsiva desarrollada con Flask en el backend, potenciada con htmx para interacciones asíncronas en tiempo real (sin recargas de página) y estilizada con Bootstrap 5.3 para lograr una interfaz limpia, elegante y moderna.

Este repositorio forma parte de mi portafolio profesional enfocado en el desarrollo web ágil y arquitecturas de backend eficientes.

🛠️ Tecnologías Utilizadas

Backend: Flask (Python 3)

Base de Datos / ORM: SQLAlchemy (SQLite integrado para desarrollo ágil)

Frontend Dinámico: htmx (Interacciones AJAX directamente a través de atributos HTML, eliminando la necesidad de frameworks SPA complejos como React o Vue para tareas CRUD tradicionales)

Estilos: Bootstrap 5.3 (Componentes responsivos, sistema de grilla y utilidades modernas de espaciado)

✨ Características Principales

Interacciones en Tiempo Real (SPA-like): Gracias a htmx, las altas, bajas y modificaciones se realizan de forma asíncrona mediante peticiones POST, DELETE, GET y PUT transparentes para el usuario.

CRUD Completo de Noticias:

Crear: Envío de noticias con asociación automática o creación instantánea de autores en segundo plano.

Leer: Listado responsivo con tipografía moderna, badges para los autores y efectos visuales de interacción.

Actualizar (Edición Inline): Al hacer clic en Editar, la fila de la tabla se transforma dinámicamente en un formulario de edición inline (table-warning) usando hx-get, permitiendo guardar o cancelar en un solo clic sin cambiar de página.

Eliminar con Animación: Las noticias se remueven con transiciones CSS suaves (htmx-swapping) coordinadas por htmx antes de retirar el elemento del DOM.

Arquitectura Limpia: Renderizado de fragmentos HTML parciales directamente desde el servidor (Server-Side Rendering de componentes), maximizando la velocidad de respuesta y simplificando el estado global de la aplicación.

📸 Demostración de Flujo (HTMX Inline Editing)

Acción

Atributo HTMX Clave

Comportamiento en el Cliente

Publicar

hx-post="/submit"

Inserta el fragmento HTML al final de la lista (beforeend)

Editar

hx-get="/get-edit-form/<id>"

Reemplaza la fila actual por el formulario de edición inline

Guardar

hx-put="/update/<id>"

Envía los datos modificados del input actual (closest tr)

Borrar

hx-delete="/delete/<id>"

Aplica desvanecimiento y remueve el elemento de la tabla

🚀 Instalación y Uso Local

Sigue estos pasos para levantar el entorno de desarrollo en tu máquina local:

1. Clonar el repositorio

git clone [https://github.com/Kenkyoo/flask-hackernews.git](https://github.com/Kenkyoo/flask-hackernews.git)
cd flask-hackernews

2. Configurar el Entorno Virtual (Recomendado)

# En Linux/macOS

python3 -m venv venv
source venv/bin/activate

# En Windows

python -m venv venv
venv\Scripts\activate

3. Instalar Dependencias

pip install -r requirements.txt

4. Inicializar la Base de Datos y Ejecutar

Asegúrate de configurar tus variables de entorno si estás usando un motor de producción, o ejecuta por defecto en modo de desarrollo:

flask run

Abre tu navegador en http://127.0.0.1:5000/ ¡y listo!

📂 Estructura Esencial del Proyecto

flask-hackernews/
│
├── app/
│ ├── **init**.py # Inicialización de la app Flask y SQLAlchemy
│ ├── models.py # Modelos de datos (New, Author)
│ └── templates/
│ └── index.html # Estructura principal optimizada con Bootstrap 5
│
├── views.py # Rutas y lógica de endpoints que retornan fragmentos HTMX
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo de documentación

🧠 Aprendizajes y Enfoque Técnico

Este proyecto demuestra los beneficios de la arquitectura HDA (Hypermedia Driven Applications):

Reducción drástica de la complejidad: Se eliminó la necesidad de configurar APIs REST complejas (JSON serializers) y escribir código JavaScript pesado para el manejo de estados del cliente. El backend maneja tanto los datos como la presentación de manera unificada.

Experiencia de usuario fluida: El usuario experimenta una navegación instantánea y sin parpadeos, idéntica a la de una Single Page Application (SPA), manteniendo la robustez y simplicidad del renderizado en el servidor de Flask.

Mantenimiento Estilizado: Al acoplar de forma precisa las clases CSS utilitarias de Bootstrap tanto en el template base como en las respuestas parciales del archivo views.py, se logra un diseño consistente y altamente escalable para el crecimiento del sitio.

Desarrollado con ❤️ enfocado en crear software eficiente, mantenible y moderno.
