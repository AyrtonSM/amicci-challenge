FROM python:3.12

WORKDIR /usr/amicci-api/app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD [ "django-admin", "startproject" , "amicci", "."]
CMD [ "django-admin", "startapp" , "api"]
CMD [ "python3", "manage.py" , "migrate"]
CMD [ "python3", "createsuperuser" , "--username", "amicci-dev", "--email", "dev@amicci-dev.com"]
CMD [ "python3", "manage.py" , "runserver", "0.0.0.0:8000"]

