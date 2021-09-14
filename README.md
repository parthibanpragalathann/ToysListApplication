# TOYS LIST Application using Django with Postgresql

## Create Database in Postgresql

## Create virtual environment and activated it.

## Requirements
### Python - 3 and above
### Django and DRF
### postgresql
## Installation:
```python
pip install -r requirements.txt

```

## Database migration
```python
python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```
## Below REST api requests all using curl.

### URL for GET and POST Retrieve all the Toys details

#### http://127.0.0.1:8000/api/toys/

### URL for PUT and DELETE Retrieve particular Toys details

#### http://127.0.0.1:8000/api/toys/<int:pk>/

### URL for GET Retrieve particular Toys details

#### http://127.0.0.1:8000/api/toy/<int:pk>/