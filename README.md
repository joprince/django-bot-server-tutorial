# How to use this branch

This part of the seminar involves installing and getting started with django channels.

To get this running, simply run the following 

## Step 1: Install requirements.txt

`pip install -r requirements.txt`

## Step 2: Create databases

Create the databases and the initial migrations with the following command:
`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`

You should now be able to go to localhost:8000/user/ and chat with the bot. Also visit localhost:8000/logs/ to view the logs
