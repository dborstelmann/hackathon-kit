Hackathon-kit
===========
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Ready made to be an instant project kit with almost no setup and easily deployable
#### The stack is made up of the following:
- PostgreSQL
- Django
    - Models
    - Views
    - Auth (including already built login, logout, and register views)
- Underscore
    - Templates
- Backbone
    - Models and Collections
    - Views
- Materialize (easily swappable to bootstrap if you prefer)
- Less
    - less.js compiles in the browser so this is not recommended for production environments

&nbsp;
## Local Setup

### 1. PostgreSQL

The first thing to do is make sure you have [PostgreSQL](https://www.postgresql.org/) downloaded, installed, and **running**.  Then either get [Postico](https://eggerapps.at/postico/ "A fantastic PostgreSQL application for Mac") or open a `psql` shell.

**Run the following commands:**

```
CREATE USER <your_username> WITH CREATEDB;
ALTER USER <your_username> WITH PASSWORD '<your_password>';
CREATE DATABASE <your_database> WITH OWNER <your_username>;
```

Now you should have a development database setup on your local machine for the app to use.

### 2. Django

Make sure you have Django installed. (If not, run `pip install django`)

Next we need to set the following variables in our bash shell so that Django knows which database to use.

**Run the following in your shell:**

```
export HACKATHON_KIT_LOCAL_NAME=<your_database>
export HACKATHON_KIT_LOCAL_USERNAME=<your_username>
export HACKATHON_KIT_LOCAL_PASSWORD=<your_password>
export DJANGO_HACKATHON_KIT_SECRET_KEY="random_string_here"
```

> Note: If you don't want to have to set these variables every single time you open a shell, you can either set them in your .bashrc (or .zshrc like me) file or you can write a script to run them for you.  Up to you.

Then we need to bring your database up to date with the state of your models.

**Run the following from your project directory in your shell:**

```
python manage.py makemigrations
python manage.py migrate
```

**All that's left is to start your server:**

```
python manage.py runserver
```

That's really all you need to get started, however I have added sections below on the one-button install to [Heroku](https://www.heroku.com/) and an explanation of the frontend stack.


## Deploying to Heroku

This project is already set up to be immediately deployed to **Heroku** through one click of the following button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

If you want to change the settings of this deployment, please visit [app.json](./app.json)
