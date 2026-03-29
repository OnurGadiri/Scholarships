# Scholarship Tracker

Django + SQLite. Layihə kodu `scholarship_tracker` qovluğundadır.

## Quraşdırma

```bash
cd scholarship_tracker
python -m venv venv
venv\Scripts\activate
pip install -r ..\requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Brauzer: http://127.0.0.1:8000/

## Qeyd

`db.sqlite3` və virtual mühit repoda yoxdur; `migrate` ilə baza yaradılır.
