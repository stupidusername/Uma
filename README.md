# Uma

Uma: Management Application


## Requirements

- Python >= 3.5 (tested on 3.7.3)
- PyPI packages listed on `requirements.txt`
    - `django-debug-toolbar` is only needed if you enable debug mode
    - `psycopg2` is only needed if you are using PostgreSQL
    - `pytest-asyncio` and `pytest-django` are only needed if you want to run the WebSocket tests
- A RDMS supported by Django (tested on PostgreSQL 11.4)


## Installation on a development environment

- Check prerequisites that need to be met in order to install `psycopg2`.
  See [build prerequisites](http://initd.org/psycopg/docs/install.html#build-prerequisites).

- Install PyPI packages.

    ```
    $ pip install -r requirements.txt
    ```

- Create a database. As an example a Docker Compose file is provided.
  The file defines a PostgreSQL container.
  It also defines and Adminer container which you can access on port `8080`.
  The server name of the PostgreSQL container is `db`.

- Create the local settings of your project in `project/settings/local.py`.
  The file `local-example.py` can serve you as an example.

- Run migrations.

    ```
    $ python manage.py migrate
    ```

- Create a super user for the admin panel.

    ```
    $ python manage.py createsuperuser
    ```


## Running tests

- `unittest` tests:

    ```
    $ python manage.py test
    ```

- WebSocket tests:

    ```
    $ pytest
    ```


## Running the development web server

```
$ python manage.py runserver
```
