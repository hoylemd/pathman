MANAGEPATH=pathman/manage.py
dev_settings=config.settings.dev

RUNCOMMAND=runserver --settings=$(dev_settings)

run: $(MANAGEPATH)
	python $(MANAGEPATH) $(RUNCOMMAND)

