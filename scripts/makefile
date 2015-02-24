MANAGE=python manage.py
RUNSQL=sqlite3 tmp.db

dump:
	$(MANAGE) dumpdata | python -m json.tool > dump.json

reset-db:
	./softdropdb.sh
	$(MANAGE) syncdb

load-core: charman/core_rulebook.json
	$(MANAGE) loaddata charman/core_rulebook.json

load-iconics: load-core charman/iconics_core.json
	$(MANAGE) loaddata charman/iconics_core.json

reset-iconics: reset-db load-iconics



