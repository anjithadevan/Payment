# Payment
This application is created for getting payment from a client for an organization.The organisation Hr enter the details of a client to db via admin and it automatically create a short url.The HR can send that to client.By clicking the link client can pay to the organization.

steps:
1.Install requirements - pip install -r requirements.txt
2.Create data base 
  a) python manage.py makemigrations
  b) python manage.py migrate
3.Create a bitley and stripe account.Put the keys in settings.
4.Run the project - python manage.py runserver

