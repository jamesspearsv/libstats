# MPL LibStats

## Introduction

MPL LibStats is a simple web app build using Django/Python, SQLite, HTML, CSS, and Javascript that helps library staff record, track, and report references interactions with library patrons. This app is a basic clone of the LibAnswers module from SpringShare's LibApps cloud platform. The goal of this project was to create a similar yet simplier tool for use in a library setting. Because of the overall goal to make this project as simple as possible, the app lacks some of the detailed recording and reporting abilities present in other reference statictics collection software in exchange for meeting the specific and most important needs of my library. This project could be extended to meet future needs or the specific needs of other libraries. With some basic technical know-how, and the ability to follow online instruction, this app is simple and lightweight enough to deploy on a locally hosted server, like a Raspberry Pi, using a WSGI and Http proxy server like Gunicorn and Nginx.

## Functions

LibStats currently includes three basic fuctions:

- Recording reference interactions
- Viewing a log of previously recorded reference interactions
- Generating reports for recorded reference interactions

### Record

This is the main function that library staff will interact with. Using this funciton, staff complete a form that included various date that is collected to represent a reference interaction with patron. When this form is submitted, a new transactions is appended to the app's database.

### View

The view function allows users view a log of recorded transactions. Users are prompted to input a desired date range and are returned a table that lists every recorded transaction during the submitted date range. This function also allows staff to export the returned table to a CSV file.

### Report

The reporting function allows staff who collect and report statistics to generate a report based on a submitted date range. Staff are asked to provide a desired range of date and the app will return a count of transactions sorted by various types of date like transaction type and format.

## Security

LibStats includes basic IP filtering to prevent unwanted users from accessing and recording bogus reference transactions. IP authentication was written using a custom middleware for Django and allowed IP are access be reading a local configuration file that is stored on the hosting server.