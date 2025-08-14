# NailPort

A Django + PostgreSQL project running with Docker Compose.

## Quick Start

- Clone the repository and navigate to the project folder:

git clone https://github.com/Aleksandar-Stoev/NailPort.git
cd NailPort
- Create .env from the example file:
cp .env.example .env
Fill in the required values.
- Start the application:
docker-compose up
App will be available at: http://127.0.0.1:8000/
- Apply migrations:
docker-compose exec web python manage.py migrate
- Create a superuser (Windows Git Bash):
winpty docker-compose run --rm web python manage.py createsuperuser
