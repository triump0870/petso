release: python src/manage.py migrate
web: gunicorn --chdir src/ petso.wsgi --preload
worker: celery --workdir=src -A petso worker --app=petso.settings.celery_app:app --loglevel=info --pool=solo