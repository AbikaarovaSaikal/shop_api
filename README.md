# Shop API

REST API for an online shop built with Django REST Framework.

## Features

* Custom user model with email authentication
* User registration
* Email confirmation with one-time code
* Login with Token Authentication
* JWT authentication
* Google OAuth login
* Product CRUD API
* Category CRUD API
* Review CRUD API
* Product rating based on reviews
* Product list caching with Redis
* Pagination
* Custom permissions
* PostgreSQL database
* Celery background tasks
* Celery Beat scheduled tasks
* Flower for Celery monitoring
* Swagger and ReDoc API documentation
* Docker and Docker Compose support

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Redis
* Celery
* Celery Beat
* Flower
* JWT
* DRF Token Authentication
* drf-yasg
* Docker
* Docker Compose

## Project Structure

```text
shop-api/
├── shop_api/            # Project settings, URLs, Celery and Swagger configuration
├── users/               # Custom user, registration, login, email confirmation, OAuth
├── product/             # Products, categories, reviews
├── common/              # Custom permissions and validators
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── manage.py
└── README.md
```

## API Endpoints

### Products

```text
GET     /api/v1/products/
POST    /api/v1/products/
GET     /api/v1/products/<id>/
PUT     /api/v1/products/<id>/
DELETE  /api/v1/products/<id>/
```

### Categories

```text
GET     /api/v1/products/categories/
POST    /api/v1/products/categories/
GET     /api/v1/products/categories/<id>/
PUT     /api/v1/products/categories/<id>/
DELETE  /api/v1/products/categories/<id>/
```

### Reviews

```text
GET     /api/v1/products/reviews/
POST    /api/v1/products/reviews/
GET     /api/v1/products/reviews/<id>/
PUT     /api/v1/products/reviews/<id>/
DELETE  /api/v1/products/reviews/<id>/
```

### Users

```text
POST    /api/v1/users/registration/
POST    /api/v1/users/login/
POST    /api/v1/users/confirm/
POST    /api/v1/users/jwt/
POST    /api/v1/users/jwt/refresh/
POST    /api/v1/users/jwt/verify/
POST    /api/v1/users/google-login/
```

### Documentation

```text
/swagger/
/redoc/
```

## Environment Variables

Create a `.env` file in the project root:

```env
SECRET=your_secret_key
DEBUG=on

DB_NAME=shop_db
DB_USER=shop_user
DB_PASSWORD=shop_password
DB_HOST=db
DB_PORT=5432

REDIS_CACHE=redis://redis:6379/1
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_CLIENT_URI=your_google_redirect_uri
```

## Run with Docker

Build and start containers:

```bash
docker-compose up --build
```

The API will be available at:

```text
http://localhost:7001/
```

Swagger:

```text
http://localhost:7001/swagger/
```

ReDoc:

```text
http://localhost:7001/redoc/
```

## Local Installation

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the project:

```bash
python manage.py runserver
```

## Status

Educational backend project created while learning Django REST Framework, authentication, PostgreSQL, Redis, Celery, Docker and API development.