release: python src/manage.py collectstatic --noinput
web: gunicorn --chdir src/ petso.wsgi --preload
