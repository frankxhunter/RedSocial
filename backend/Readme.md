# Creacion del ambiente virtual
py -m venv mi-ambiente-virtual
# Activacion del ambiente virtual
./mi-ambiente-virtual/Scripts/activate

# Instalacion de dependencias
pip install django
pip install djangorestframework
pip install django-cors-headers

# Correr proyecto
py manage.py runserver