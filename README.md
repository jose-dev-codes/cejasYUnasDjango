# Cejas y Uñas — Módulo de Citas (Django)

CRUD de gestión de citas para salón de belleza, construido con Django y PostgreSQL.

## Requisitos previos

- Python 3.10 o superior
- PostgreSQL instalado y corriendo
- Git

## Instalación

### 1. Clonar el repositorio

\`\`\`bash
git clone https://github.com/jose-dev-codes/cejasYUnasDjango.git
cd cejasYUnasDjango
\`\`\`

### 2. Crear y activar el entorno virtual

\`\`\`bash
python -m venv .venv
.venv\Scripts\activate
\`\`\`

### 3. Instalar dependencias

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Crear la base de datos

En PostgreSQL (por ejemplo, con DBeaver o psql), crea una base de datos vacía. El nombre puede ser el que prefieras, por ejemplo `crud_salon`.

### 5. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con este contenido, ajustando los valores a tu entorno:

\`\`\`
SECRET_KEY=cualquier_texto_largo_y_aleatorio
DB_NAME=crud_salon
DB_USER=postgres
DB_PASSWORD=tu_contraseña_de_postgres
DB_HOST=localhost
DB_PORT=5432
\`\`\`

### 6. Ejecutar las migraciones

\`\`\`bash
python manage.py migrate
\`\`\`

### 7. Cargar los datos de prueba

\`\`\`bash
python manage.py loaddata datos_prueba.json
\`\`\`

### 8. Levantar el servidor

\`\`\`bash
python manage.py runserver
\`\`\`

Abre en el navegador: `http://127.0.0.1:8000/citas/`

## Funcionalidades

- Listado de citas con paginación (10 por página)
- Crear, editar y eliminar citas
- Validación de horario: un mismo especialista no puede tener dos citas activas a la misma fecha/hora
- No se puede crear una cita directamente con estado "Cancelada"
