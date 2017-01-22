# Django Imager
[![Build Status](https://travis-ci.org/ellezv/django_imager.svg?branch=models-2)](https://travis-ci.org/ellezv/django_imager)
**Author:** Julien Wilson and Maelle Vance


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
(django_lender) $ pip install -r requirements.pip
```

Navigate to the project root, `imagersite`, and apply the migrations for the app.

```bash
(django_lender) $ cd imagersite
(django_lender) $ ./manage.py migrate
```

Finally, run the server in order to server the app on `localhost`

```bash
(django_lender) $ ./manage.py runserver
```

Django will typically serve on port 8000, unless you specify otherwise.
You can access the locally-served site at the address `http://localhost:8000`.

## Running Tests

Running tests for the `django_imager` is fairly straightforward.
Navigate to the same directory as the `manage.py` file and type:

```bash
(django_lender) $ ./manage.py test
```

This will show you which tests have failed, which tests have passed.


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

## Current URL Routes

- `/admin`
- `/login`
- `/logout`
- `/registration/register/`