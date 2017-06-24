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

5. Go to http://localhost:8000/index/

I got the DB population, search and viewing of content from the DB working. But I couldn't get new entries added to the shopping cart. I kept having trouble writing to the date fields and gave up after numerous attempts.
