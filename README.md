# Django Imager
[![Build Status](https://travis-ci.org/ellezv/django_imager.svg?branch=front_end_4)](https://travis-ci.org/ellezv/django_imager)
[![Coverage Status](https://coveralls.io/repos/github/ellezv/django_imager/badge.svg?branch=front_end_4)](https://coveralls.io/github/ellezv/django_imager?branch=front_end_4)

**Author:** Julien Wilson and Maelle Vance

**Django Imager** is a full Django app that allows you to upload your personal images and share them with the world. You create and manage albums, add new photos to different albums or edit any of them.

## Getting Started

Clone this repository into whatever directory you want to work from.

```bash
$ git clone https://github.com/ellezv/django_imager.git
```

Assuming that you have access to Python 3 at the system level, start up a new virtual environment.

```bash
$ cd django_imager
$ python3 -m venv venv
$ source venv/bin/activate
```

Once your environment has been activated, make sure to install Django and all of this project's required packages.

```bash
(venv) $ pip install -r requirements.pip
```

Navigate to the project root, `imagersite`, and apply the migrations for the app.

```bash
(venv) $ cd imagersite
(venv) $ ./manage.py migrate
```

Finally, run the server in order to server the app on `localhost`

```bash
(venv) $ ./manage.py runserver
```

Django will typically serve on port 8000, unless you specify otherwise.
You can access the locally-served site at the address `http://localhost:8000`.

## Running Tests

Running tests for the `django_imager` is fairly straightforward.
Navigate to the same directory as the `manage.py` file and type:

```bash
(venv) $ coverage run ./manage.py test
```

This will show you which tests have failed, which tests have passed.

To get the full coverage report, after you have run the tests, type:

```bash
(venv) $ coverage report -m
```


## Current Models (outside of Django built-ins)

*ImagerProfile*

- user (related to the built-in User)
- address (unicode)
- bio (unicode)
- website (unicode)
- hireable (boolean, defaults to True)
- travel radius (integer)
- phone number (unicode)
- camera type (choice field)
- photography type (choice field)
- is active (boolean)
- api "ImageProfile.active" returns a query set of all active users


*Image*

- title (unicode)
- description (unicode)
- date published (datetime)
- date modified (datetime)
- date uploaded (datetime)
- published (choicefield : private, shared or public)
- image (imagefield)
- owner (related to ImagerProfile)


*Album*

- title (unicode)
- description (unicode)
- date published (datetime)
- date modified (datetime)
- date created (datetime)
- published (choicefield: private, shared or public)
- cover image : (imagefield)
- owner (related to ImagerProfile)
- images (related to Image model)

## Current URL Routes

- `/admin`
- `/login`
- `/logout`
- `/registration/register/`
- `/profile`
- `/profile/username`
- `/images/library/`
- `/images/photos/`
- `/images/albums/`
- `/images/photos/(pk)/`
- `/images/albums/(pk)/`
- `/images/photos/add/`
- `/images/albums/add/`
- `/images/albums/(pk)/edit/`
- `/images/photos/(pk)/edit/`
