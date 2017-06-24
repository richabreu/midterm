FROM python:3.4
ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt
EXPOSE 8000
RUN pip install mysqlclient
RUN pip install -r requirements.txt
RUN mkdir /var/djangoproject
WORKDIR /var/djangoproject