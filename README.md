# NailPort

A Django + PostgreSQL project running with Docker Compose.

## Quick Start

1. Clone the repository and navigate to the project folder:
git clone https://github.com/Aleksandar-Stoev/NailPort.git
cd NailPort

2. Create .env from the example file:
cp .env.example .env
Fill in the required values.

3. Start the application:
docker-compose up
App will be available at: http://127.0.0.1:8000/

4. Apply migrations:
docker-compose exec web python manage.py migrate

5. Create a superuser (Windows Git Bash):
winpty docker-compose run --rm web python manage.py createsuperuser

Useful Commands

# Make and apply migrations
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput

# Open Django shell
docker-compose exec web python manage.py shell