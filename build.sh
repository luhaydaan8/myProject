pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

if [ -n "$SECRET_SUPERUSER" ]; then
    python manage.py createsuperuser --no-input
fi
