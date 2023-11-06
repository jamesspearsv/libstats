# MPL LibStats

## Introduction

MPL LibStats is a simple web app build using Django/Python, SQLite, HTML, CSS, and Javascript that helps library staff record, track, and report references interactions with library patrons. This app is a basic clone of the LibAnswers module from SpringShare's LibApps cloud platform. The goal of this project was to create a similar yet simplier tool for use in a library setting. Because of the overall goal to make this project as simple as possible, the app lacks some of the detailed recording and reporting abilities present in other reference statictics collection software in exchange for meeting the specific and most important needs of my library. This project could be extended to meet future needs or the specific needs of other libraries. With some basic technical know-how, and the ability to follow online instruction, this app is simple and lightweight enough to deploy on a locally hosted server, like a Raspberry Pi, using a WSGI and Http proxy server like Gunicorn and Nginx.

## Functions

LibStats currently includes three basic fuctions:

- Recording reference interactions
- Viewing a log of previously recorded reference interactions
- Generating reports for recorded reference interactions

Each of the above funcitons is accessed through the app's views.py file.

### Record

This is the main function that library staff will interact with. Using this funciton, staff complete a form that included various date that is collected to represent a reference interaction with patron. When this form is submitted, a new transactions is appended to the app's database.

### View

The view function allows users view a log of recorded transactions. Users are prompted to input a desired date range and are returned a table that lists every recorded transaction during the submitted date range. This function also allows staff to export the returned table to a CSV file.

### Report

The reporting function allows staff who collect and report statistics to generate a report based on a submitted date range. Staff are asked to provide a desired range of date and the app will return a count of transactions sorted by various types of date like transaction type and format.

## Docker Configuration

Libstats has been set up to be deployed using docker and docker-compose. The _docker-compose.yml_ file creates two containers. First a gunicorn container is created to run and serve the libstats django app using gunicorn. In this container, dependencies are installed using requirements.txt. Then any database mirgations are applied and static files collected using entrypoint.sh. Second an nginx container is created to serve as a proxy server and to serve static files for libstats. The configurtion for this contianer is within _nginx_.

To complete the Docker configuration, you will need to create one directory and several files. First, in the root of this project you must create a _data_ directory. This is the data directory that contains that database file and django configurtion options. With in this directory first create _db.sqlite3_. This will be the persistent database file that libstats will read from and write to by default. You can change this by editing libstats' _settings.py_ file.Next you will need to create a _libstats-config.json_ file. This file stores several configurtion option for libstats that are read by _settings.py_ An example of this file is below:

```
{
    "ALLOWED_HOSTS": ["UPSTREAM_NGINX_SERVER", "HOST_IP"],
    "SECRET_KEY": "MAKE_SURE_TO_SET_A_SECRET_KEY",
    "CSRF_TRUSTED_ORIGINS": ["http://HOST_IP:NGINX_PORT"]
}
```

Both containers read and write static files to and from the _static_ volume that is created in _docker-compose.yml_. You could map this to a location in the root of the directory or other location on your system if needed. For example if you needed to build static files before running your containers and then wanted to inject them into your containers.

Make sure to check that the default container ports are available on your system in _docker-compose.yml_. By default gunicorn listens on port 8080 and nginx listens on port 80. This both map to ports 8080 and 8090 on the host system by default. Adjust them according if they are not availabe on your system. If you change the port that the gunicorn container listens on, remember to make that change in _nginx/default.conf_.

Once you have the correct configuration files in _data_ you can then run `docker compose up -d --build` to build the images and create the containers. Use `docker compose up` to run libstats in the foreground.
