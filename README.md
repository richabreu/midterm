# midterm
midterm project
Rich Abreu midterm project

Brief instructions as performed on my Windows 10 PC

mysql schemaname used is "midterm"

1. Powershell to root directory:
docker-compose build
docker-compose up

2. Second Powershell bash:
docker exec -it dockermidterm_django_1 bash

3. Build DB:
python manage.py makemigrations midterm
python manage.py migrate

4. Populate DB:
python populate_midterm.py
