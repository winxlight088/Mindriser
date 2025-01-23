<!-- install virtual environment --->
 pip install virtualenv

<--create env file-->
python -m venv env

<--gitinnore file -->
go to google and copy paste gitignore file from https://www.toptal.com/developers/gitignore

 <!-- activate virtual environment in cmd>-->
 env\Scripts\activate

<!-- create project-->
django-admin start project myproject1 .

 <!-- Install django in terminal-->
 pip install django

<!-- create app-->
<!-- python manage.py <app_name>-->
python manage.py startapp todo

<!-- run django-->
python manage.py runserver

<!-- INSTALL requirements-->
pip install -r requirements.txt 
or 
pip freeze > requirements.txt


<!-- to open python shell-->
python manage.py shell


<!-- create data in terminal-->
<Model_name>.objects.create(field1="..",field2="..",field3=".." )

<!-- Get all the data of the model-->
<Model_name>.objects.all()

<!-- Get single data of the model-->
<Model_name>.objects.get(fieldyouwanttoget = "", or id =1)

<!-- Filter data-->
<Model_name>.objects.filter(fields = "", field2 = "")

<!-- save the data-->
<Model_name>.save()

<!-- delete datal-->
<Model_name>.delete()

<!-- activate/create/add adminuser-->
python manage.py createsuperuser




