# Getting started with Django no BS

## Set up virtual environment

- You can use pipenv,conda,venv e.t.c or any other package manager to set up a virtual environment.But i prefer pipenv as it is easy to keep track of all the packages installed in the virtual environment so there is no need for a requirements.txt.
<!-- why use virtual environment -->

### Install Pipenv

- Make sure you have python and pip installed.
- Run the following command to install pipenv:
  `pip install pipenv`

### Create Project Directory and Activate Virtual Environment

- To create a project directory, run the following command:
  `mkdir my_project && cd my_project`
- To install Django run the following command:
  `pipenv install django`
- At this point you should have two files in your project directory:
  `Pipfile` and `Pipfile.lock` if your familiar with nodejs these files look like package.json and they work similarly.
- To activate the virtual environment, run the following command:
  `pipenv shell`
- You should now see (my_project) before your prompt, `(my_project)$`, indicating that you’re running within the ‘my_project’ virtual environment.

### Initialize Django Project

- To initialize a Django project, run the following command:
  `django-admin startproject my_project .` _we add the dot at the end to create the project in the current directory_
- This should be your folder structure now

```bash
├── my_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

- To test if your app was properly installed run the following command:
  `python manage.py runserver` _this will start a development server on port 8000 then you can visit http://localhost:8000/ to see your app_ .To exit press ctrl+c to stop the server.

### Create Environement Variables for Django

https://djecrety.ir/
https://blog.saurav-shrivastav.tech/setting-up-a-basic-django-project-with-pipenv
https://djoser.readthedocs.io/en/latest/getting_started.html


<!--  -->
$ pip install mysqlclient

