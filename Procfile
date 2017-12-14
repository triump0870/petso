release: python src/manage.py migrate
web: gunicorn --chdir src/ petso.wsgi --preload
