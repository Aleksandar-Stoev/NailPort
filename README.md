# NailPort

A Django + PostgreSQL project running with Docker Compose.

## Quick Start

1. Clone the repository and navigate to the project folder:
```bash
git clone https://github.com/Aleksandar-Stoev/NailPort.git
cd NailPort
Create .env from the example file:

bash
Copy
Edit
cp .env.example .env
Fill in the required values.

Start the application:

bash
Copy
Edit
docker-compose up
App will be available at: http://127.0.0.1:8000/

Apply migrations:

bash
Copy
Edit
docker-compose exec web python manage.py migrate
Create a superuser (Windows Git Bash):

bash
Copy
Edit
winpty docker-compose run --rm web python manage.py createsuperuser
.env.example
env
Copy
Edit
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=1

POSTGRES_DB=nail_port
POSTGRES_USER=postgres-user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
Useful Commands
bash
Copy
Edit
# Make and apply migrations
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput

# Open Django shell
docker-compose exec web python manage.py shell