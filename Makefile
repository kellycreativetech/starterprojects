all: devsite

clean:
	rm -rf /tmp/_build;

devsite:
	mkdir /tmp/_build;
	cd /tmp/_build; \
		virtualenv env; \
		source env/bin/activate; \
		rm -rf testsite; \
		django-admin.py startproject testsite --template=$(CURDIR); \
		dropdb testsite; \
		createdb testsite; \
		cd testsite; \
			pip install -r requirements.txt; \
			python manage.py syncdb --noinput; \
			python manage.py runserver;
