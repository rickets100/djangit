<!-- ========= GETTING STARTED ========== -->

1) Install PIP
> sudo easy_install pip

2) Install Django
> pip install Django

3) Install PostgreSQL driver if switching from SQLite
> pip install django-pgjson

4) To create a new Django project, navigate to a folder where you want to create the project, then:
> django-admin startproject <NAME_OF_YOUR_PROJECT>

5) Inside that new project you will find a settings.py file, open it and find the DATABASE =  section and change it to:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'NAME_OF_YOUR_DATABASE', # this DB has to be created in postgres first
        'USER': 'YOUR_USERNAME',
        'PASSWORD': 'YOURPASSWORD',
        'HOST': 'localhost',                      
       'PORT': '',                      
   }
}

6) cd into the project and look for the manage.py file. All these later commands are issued from that folder

7) To start the test server: (defaults to port 8000)
> python manage.py runserver

OR: to start the test server on port 80 (default web port)
> sudo python manage.py runserver 0.0.0.0:80


<!-- ============= MIGRATIONS ============== -->
8) If you create a new Model or modify an existing one, you need to create a migration
> python manage.py makemigrations

9) Run the migration
> python manage.py migrate

10) to create a superuser so you can log into the autogenerated admin
> python manage.py createsuperuser

if migrations get all screwy:
./manage.py migrate djangit zero
then delete (manually) everything in the migrations folder EXCEPT __init__.py
python manage.py showmigrations to show status
python manage.py makemigrations
python manage.py migrate
https://www.youtube.com/watch?v=UpssHYl6bjA&index=7&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK
the above video at the 10:42 mark has foreign key example
https://docs.djangoproject.com/en/1.10/topics/migrations/

migration-serializing
 .schema at the client command line

sqlmigrate at the command line just prints it to the screen so that you can see what SQL Django thinks is required - doesn't actually do a migration

python manage.py check; this checks for any problems in your project without making migrations or touching the database

to filter: Hop.objects.filter(hop_name__startswith='C')


<!-- ========= FORMS ==========  -->
https://docs.djangoproject.com/en/1.11/topics/forms/

HIDDEN FIELD EXAMPLE:
<input type="hidden" name="id" value="{{lostitem.id}}">

<!-- <form method="POST" action={% if id %}"/hops/{{ id }/editHop"{% else %}"/hops/" {% end %} class="well"> -->

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
https://docs.djangoproject.com/en/1.10/ref/validators/


FOR IMPLEMENTING CHOICES DOWN THE ROAD
--------------------------------------
CITRUSY = 'CI'
FLORAL = 'FL'
FRUITY = 'FR'
FUNKY = 'FU'
GRASSY = 'GS'
HERBAL = 'HE'
HOPPY = 'HO'
PINEY = 'PI'
SPICY = 'SP'
AROMA_CHOICES = (
    (CITRUSY, 'Citrusy'),
    (FLORAL, 'Floral'),
    (FRUITY, 'Fruity'),
    (FUNKY, 'Funky'),
    (GRASSY, 'Grassy'),
    (HERBAL, 'Herbal'),
    (HOPPY, 'Hoppy'),
    (PINEY, 'Piney'),
    (SPICY, 'Spicy'),
)
aroma = models.CharField(
    max_length=2,
    choices=AROMA_CHOICES,
    default=HOPPY,
)


<!-- ======== URL PATTERNS ======== -->
url(regex, view, kwargs, name)

djangit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))


<!-- ====== OTHER USEFUL INFO FOR FUTURE ======= -->
one option for logging is: print request.method

Source code for django.template.context:
http://django.readthedocs.io/en/latest/_modules/django/template/context.html

Good basic info on working with GET and POST parameters:
http://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/

Static files (CSS, JavaScript, Images)
https://docs.djangoproject.com/en/1.11/howto/static-files/
