set 
pip install .r requirement.txt
python manage.py collectstatic --
python manage.py migrate
if[SECRET_SUPERUSER];
then
python manage.py createsuperuser --no-input