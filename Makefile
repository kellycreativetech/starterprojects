all: devsite

clean:
	rm -rf /tmp/_build;

devsite:
	mkdir /tmp/_build;
	cd /tmp/_build; \
		virtualenv env; \
		source env/bin/activate; \
		django-admin.py startproject --template=$(CURDIR) --extension=conf,py,txt,md,rst testsite ; \
		dropdb testsite; \
		createdb testsite; \
		cd testsite; \
			pip install -r requirements.txt; \
			python manage.py syncdb --noinput; \
			python manage.py runserver;

## Use the smallbuild if there are no requirements changes
smallbuild:
	cd /tmp/_build; \
		source env/bin/activate; \
		rm -rf testsite; \
		django-admin.py startproject --template=$(CURDIR) --extension=conf,py,txt,md,rst testsite ; \
		dropdb testsite; \
		createdb testsite; \
		cd testsite; \
			python manage.py syncdb --noinput; \
			python manage.py runserver;
