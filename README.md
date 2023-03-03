Acme application login
=============
# Installation Steps with Python Virtualenv

First, ensure that you have virtualenv installed on your local machine. You can install it using the following command:

<code>
    pip install virtualenv
</code>

Next, create a new virtual environment for this app and activate it:

<code>
    virtualenv venv
    <br>
    .\venv\Scripts\activate
</code>

Install all the required dependencies for local development:

<code>
    pip install -r requirements.txt
</code>

Apply all the migrations:

<code>
    python manage.py migrate
</code>

Finally, run the app:

<code>
    pip manage.py runserver
</code>

# Installation Steps with Docker

Ensure that you have Docker installed on your computer:

<code>
    docker --version
    <br>
    docker-compose --version
</code>

Build the Docker image for the app:

<code>
    docker-compose build
</code>

Start all the required services:

<code>
    docker-compose up
</code>

# Testing the Application Functions
You can try the following application routes, all of which use the POST method

- /users/login
- /users/signup
- /users/sign-out
