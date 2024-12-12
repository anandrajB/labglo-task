
#  LabGlo Django Task


## TECHNOLOGY STACK
[![https://www.python.org/](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/)




Make sure you have the following installed on your machine:

- docker (optional)
- python
- pip


## LINKS 

- [API Docs](https://labglo-task.onrender.com/docs/redoc)


#### Required packages

- [Python](https://www.python.org/downloads/) (3.11 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [flake8](https://pypi.org/project/flake8/)
- [pylint](https://pypi.org/project/pylint/)


### Run locally

1. clone the repo : `https://github.com/anandrajB/labglo-task.git`
2. Navigate to backend  : `cd labglo-task`
3. Create a virtual environment: `python3 -m venv env`
4. Activate the virtual environment:
   - For Windows: `env\Scripts\activate`
   - For Unix/macOS: `source env/bin/activate`

```
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py migrate --run-syncdb
- python manage.py collectstatic
- DJANGO_SETTINGS_MODDULE = myproject.settings 
- pytest 
- python manage.py check --deploy
- python manage.py runserver
```
 
### Run via docker

#### do the collecstatic and migrations

```bash
docker-compose run django python manage.py collectstatic
docker-compose run django python manage.py makemigrations
docker-compose run django python manage.py migrate
```

#### create superuser if required

```bash
docker-compose run django python manage.py createsuperuser
```

#### build and run

```bash
docker-compose build
docker-compose up
```
