This is mike's Pathfinder character manager

To run in dev:
- `my_scripts/go`

To run in prod:
python manage.py --settings=config.settings.prod

To add a dependancy:
- `my_scripts/add_dependancy <pip package name>`
- This will install the named dependancy with pip, and update `requirements.txt`

To start a new branch:
- `my_scripts/start <branch name>`
- Creates a local branch wit <branch name> as it's name, and pushes it to origin
