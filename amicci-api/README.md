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


### Production
There's a production application deployed, you can access it here <br> 
`http://ec2-44-223-70-169.compute-1.amazonaws.com:8000/briefings/` 

You can use `/briefings` , `/retailers`, `/vendors`, `/categories` <br>

All of them works with POST, GET, PUT verbs. 

`POST -> http://ec2-44-223-70-169.compute-1.amazonaws.com:8000/categories/`

`{ "name": "A brand new Category" }`

Fetches all <br>
`GET -> http://ec2-44-223-70-169.compute-1.amazonaws.com:8000/categories/`


Fetch a specific id <br>
`GET -> http://ec2-44-223-70-169.compute-1.amazonaws.com:8000/categories/{id_here} ` <br>

Update a specific id <br>
`PUT -> http://ec2-44-223-70-169.compute-1.amazonaws.com:8000/categories/{id_here}` <br>

`{ "name": "An Updated Category" }`