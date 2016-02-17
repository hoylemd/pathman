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
- Create a postgres User and Database named 'pathman'
-- `my_scripts/init_dev_db`
- install dependancies with pip
-- `my_scripts/install`
- run migrations with manage.py
-- `my_scripts/migrate`
- import seed data with manage.py (TODO)

Dev commands
============

To install pip dependancies:
- `my_scripts/install`

To create the dev db and user:
- `my_scripts/init_dev_db`

To apply all migrations
- `my_scripts/migrate`

To run in dev:
- `my_scripts/go`

To run in prod:
- `python manage.py --settings=config.settings.prod`

To remove the dev db:
- `my_scripts/drop_dev_db`

To rollback/migrate to a specific numbered migration
- `my_scripts/migrate <migration number>`
