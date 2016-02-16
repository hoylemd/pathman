Pathman
-------

This is mike's Pathfinder character manager

Requirements
============

- pip
- [Postgres](http://www.postgresql.org/download/)

Installation
============

- Install Postgres
- Create a 'pathman' user in postgres, with password 'password'
- Create a postgres Database named 'pathman'
- install dependancies with pip
- run migrations with manage.py
- import seed data with manage.py

Dev commands
============

To run in dev:
- `my_scripts/go`

To run in prod:
python manage.py --settings=config.settings.prod
