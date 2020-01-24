# coffee_api

**Author**: Raven Delaney
**Version**: 1.0.0

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->
Continuation of learning Django and Django REST framework

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
Uses python, command line, vs code, docker, and github

Install Django and django rest framework

Enter shell environment

Build out model, add serializer, permissions, views

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. This is also an area which you can include any visuals; flow charts, example usage gifs, screen captures, etc.-->
Uses django, djangorestframework, docker, python3, command line, github, psycopg2

## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->
When running app, check database settings in coffee_shops/settings.py

If running locally, use sqlite

Right now this is the backend frame for a website

Database has been added

Permissions can be changed

when running gunicorn bind, if it can't connect to your attempted port, try a different port number.

## Change Log

<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:
01-01-2001 4:59pm - Added functionality to add and delete some things.
-->

* 1/21/20 4:30pm - repo initialized
* 1/21/20 6:15pm - Readme updated, most of lab requirements hit
* 1/22/20 3:30pm - Gunicorn/JWT installed and applied
* 1/23/20 11:00am - .env/settings added
