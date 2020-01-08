import os
from fabric.api import local

URL_POSTGRES = 'postgres://postgres:password@localhost:5432/teatro_db'
def run():
    os.environ.setdefault('DEBUG', 'True')
    os.environ.setdefault('DATABASE_URL', URL_POSTGRES)
    os.environ.setdefault('TOOLBAR', 'True')

    local('python manage.py runserver 0.0.0.0:8000')

def test():
    os.environ.setdefault('DEBUG', 'True')
    local('python3 manage.py test')

def shell_plus():
    os.environ.setdefault('DEBUG', 'True')
    os.environ.setdefault('DATABASE_URL', URL_POSTGRES)
    local('python manage.py shell_plus')

def makemigrations():
    os.environ.setdefault('DEBUG', 'True')
    os.environ.setdefault('DATABASE_URL', URL_POSTGRES)
    local('python manage.py makemigrations')

def migrate():
    os.environ.setdefault('DEBUG', 'True')
    os.environ.setdefault('DATABASE_URL', URL_POSTGRES)
    local('python manage.py migrate')

def createsuperuser():
    os.environ.setdefault('DEBUG', 'True')
    os.environ.setdefault('DATABASE_URL', URL_POSTGRES)
    local('python manage.py createsuperuser')
