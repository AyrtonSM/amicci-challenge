# Amicci API

This project refers to amicci's api.

Create a virtual env for the project <br>
`$ python -m venv amicci-env` <br>

Activate the virtual env <br>
`$ amicci-env\Scripts\activate` <br>

Install all requirements by executing the prompt below <br>
`$ pip install -r requirements.txt` <br>

Initialize the project <br>
`$ django-admin startproject amicci .` <br>

Start the main django files for the app <br>
`$ django-admin startapp api` <br>

Initialize database by doing initial migrate <br>
`$ python manage.py migrate` <br>


Create your user, for example: <br>
`$ python manage.py createsuperuser --username amicci-dev --email dev@amicci-dev.com` <br>
Then apply your password

Run the server: <br>
`$ python manage.py runserver` <br>

## Docker
Run docker compose <br>
`$ docker compose -f compose.api.yaml up -d` <br>

Access api via: <br>
`$ http://127.0.0.1:8000/` <br>
