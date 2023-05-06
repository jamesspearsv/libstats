# Reference Stats Todo List

This is a personal project to create a reference transaction statics app for use in a public library. Similar to a clone of SpringShare's LibAnswers modules.

Initial deployment of app was on 4/21/2023
---
# TODO Lists

## Back End Tasks

- [x] Set up initial Django project and apps
- [x] Create database model(s)
- [x] Set up Admin interface
- [x] Create model form in view
- [x] Add ability to update model from front-end
- [x] Implement front-end model read function
- [x] Add reports function: return count of transactions by type and format for each location and specified dates
- [x] Adjust view function to return list of transactions at all locations in specified date 
range
- [x] Configure error and 404 pages
- [ ] Implement user sessions for admin dashboard

## Front End Tasks

- [x] Style page layout
- [x] Create site navigation
- [x] Style forms and add lable where needed
- [x] Style transaction results table
- [x] Implment CSV export and download function
- [x] Add bootstrap error and success banners
---
# Bugs
- [ ] transactions/views.py (view): Attempting to view a range of dates without any transactions returns and empty set of results. Should return a view that state this for to the user.
- [ ] transactions/views.py (view): User can attempt to qurey a range of dates with an end date prior to the given start date. Should return an error to the user.