# LibStats

## About

MPL LibStats is a simple web app built using Python, Django, SQLite, HTML, CSS, and Javascript that helps library staff record, track, and report reference interactions with library patrons. This app is a basic clone of the LibAnswers module from SpringShare's LibApps cloud platform. The goal of this project was to create a similar yet simpler tool for use in a library setting. 

Because of the overall goal to make this project as simple as possible, the app lacks some of the detailed recording and reporting abilities present in other reference statistics collection software in exchange for meeting the specific and most important needs of my library. This project could be extended to meet future needs or the specific needs of other libraries. 

With some basic technical know-how, and the ability to follow online instructions, this app is simple and lightweight enough to deploy on a locally hosted server, like a Raspberry Pi, using a WSGI and HTTP proxy server like Gunicorn and Nginx. This project specifically is designed to be deployed using Docker and Docker-Compose.

## App Functionality

LibStats currently includes three basic functions:

- Recording reference interactions
- Viewing a log of previously recorded reference interactions during a specified date range
- Generating reports for recorded reference interactions by transaction type and format during a specified date range

-----

# Getting Started

# Prerequisites

To get started using Libstats you will need to install:
- Python >= 3.7
- Django 
- Gunicorn
- Docker
- Docker-Compose

Install these using `requirements.txt` and pip, `Pipfile` and pipenv, or other python virtual environment tool.


## Docker Configuration

Libstats has been set up to be deployed using docker and docker-compose. The `docker-compose.yml` file creates two containers. 

- First, a Gunicorn container is created to run and serve the libstats Django app using Gunicorn. In this container, dependencies are installed using `requirements.txt`. Then any database migrations are applied and static files are collected using `entrypoint.sh`. The configuration for this container is within the project root.
- Second, an nginx container is created to serve as a proxy server and to serve static files for libstats. The configuration for this container is within `/nginx`.

To complete the Docker configuration, you will need to create `/data` in the root of the project and two files: `db.sqlite3` and `libstats-config.json`

```
.
├── data/
│   ├── db.sqlite3
│   └── libstats-config.json
```

`db.sqlite3` is the persistent database the libstats will read from and write to. Any migrations will be applied to the database by `entrypoint.sh` when the Gunicorn container is created and run.

`libstats-config.json` is a file that stores several configuration options for the Django backend that are read by `settings.py`. An example of this file is below:

```
{
    "DEV_MODE": true or false,
    "DEBUG": true or false,
    "ALLOWED_HOSTS": ["NGINX_UPSTREAM_NAME"],
    "SECRET_KEY": "MAKE_SURE_TO_SET_A_SECRET_KEY",
    "CSRF_TRUSTED_ORIGINS": ["http://HOST:NGINX_CONTAINER_PORT"]
}
```

Both containers read and write static files to and from the `static` volume that is created in `docker-compose.yml`. You could map this to a location in the root of the directory or another location on your system if needed. For example, if you needed to build static files before running your containers and then wanted to inject them into your containers.

Make sure to check that the default container ports are available on your system in `docker-compose.yml`. By default, Gunicorn listens on port 8080 and nginx listens on port 80. These are mapped to ports 8080 and 8090 on the host system by default. Adjust them according if they are not available on your system. If you change the port that the Gunicorn container listens on, remember to make that change in `/nginx/default.conf`.

A completed configuration should resemble the following:

```
.
├── data/
│   ├── db.sqlite3
│   └── libstats-config.json
├── libstats/
│   ├── reference/
│   │   └── settings.py
│   └── transactions/
│       ├── models.py
│       ├── urls.py
│       ├── util.py
│       └── views.py
├── nginx/
│   ├── Dockerfile
│   └── default.conf
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── Pipfile
├── README.md
└── requirements.txt
```

Once you have the correct configuration files in `/data` you can then run `docker compose up -d --build` to build the images and create the containers. 
- Use `docker compose up` to run libstats in the foreground. 
- Use `docker compose down` to stop and remove each contain should you need to make changes to the config files.

## Development Mode

To place libstats into development mode, you will need to create `libstats-config.json` in `/data` with at least the following lines:

```
{
    "DEV_MODE": true or false,
    "DEBUG": true or false
}
```

You should be able to adjust the vaules in your production `libstats-config.json` as needed if you have made this.

You will need a development database in `/libstats`for the app to work in development mode. Use `python manage.py migrate` to make a new database or copy over an existing database you want to use named `db.sqlite3`.

Once you have the development environment set up run the following to make any migrations and run the Django dev server by using `python manage.py runserver`

If you make any changes to the models make sure you remember to run `python manage.py makemigrations`

Make a superuser by running `python manage.py createsuperuser`

Use `python manage.py runserver 0.0.0.0:8000` to access the development server on your machine's local ip at port 8000.
