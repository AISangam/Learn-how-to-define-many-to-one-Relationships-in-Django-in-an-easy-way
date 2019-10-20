# Learn-how-to-define-many-to-one-Relationships-in-Django-in-an-easy-way
Learn how to define many to one Relationships in Django in an easy way   

![Django_Models](https://user-images.githubusercontent.com/35392729/67158886-9c380000-f35b-11e9-868a-016d78391ede.png)  

## How to run the code  
First step to define the database you want to use in the settings.py file [Learn-how-to-define-many-to-one-Relationships-in-Django-in-an-easy-way/orm/orm/settings.py]. I have used mysql and hence please fill the credentials there for yours. Remember to use databases with the django such as mysql one need to use client library for it like mysqlclient for mysql. I have added <strong>requirements.txt</strong> file so all these dependencies will be installed with it.  

Once you have set the right credentials for database you are using (name of database, user and password), it is the time to install the dependencies. Please run the below command to install these.  

```
pip3 install -r requirements.txt
```   

I request as well as urge the readers to create and install virtualenv for running this project. Please use the below link to install and create virtualenv for both python 2 and python 3.  

[Installing and Creating Virtual Environment using pip](https://drive.google.com/file/d/1ZOZAw57XccOskV7tL7de6k0aLeuRhhrt/view?usp=sharing)    

I hope, readers are with me and now let us proceed further. Now it is the time to perform migrations so that tables can be migrated to the database.  

To migrate django defined tables first please run the below command  
```
python3 manage.py migrate
```     
![migrate_command](https://user-images.githubusercontent.com/35392729/67159213-6dbc2400-f35f-11e9-84ba-ea4d2ece07b3.png)  

Now let us make migrations of the django user models which we have created in the models.py along with their fields. To do so please run the below commmand.    

```
python3 manage.py makemigrations  
```

Now, it the time to migrate user defined models to the database. For this please run migrate command again.  
```
python3 migrate
```
![migrate_again](https://user-images.githubusercontent.com/35392729/67159253-d4d9d880-f35f-11e9-96c7-9bf49509ab6d.png)  

Since, you are successfully in migrations, now it the time to create the superuser. Please run the below command to create the superuser. 
```
python3 manage.py createsuperuser
```
![superuser](https://user-images.githubusercontent.com/35392729/67159318-6e08ef00-f360-11e9-863c-f6e925f5c4dc.png)  

At last, it is the time to run the application. Please run the below command
```
python3 manage.py runserver
```

Note: There is nothing to show from this application but this application is to study models.py to understand how to define many to one relationships in Django.

Let us recall the steps

<ol>
  <li> python3 manage.py migrate </li>
  <li> python3 manage.py makemigrations </li>
  <li> python3 migrate </li>
  <li> python3 manage.py createsuperuser</li>
  <li> python3 manage.py runserver</li>
</ol> 

## Question to answer  

<strong>There is no source from where data is coming so how data is inserted in the database?</strong>  
<em>Solution</em>: Django is based on Object-relational mapping and hence data is inserted by entering the shell and creating the instance of classes (Newspaper and readers).  

<strong> How to enter shell?</strong>  
<em>Solution</em>: Shell is entered using the command   
```
python3 manage.py shell  
```
Thanks for reading Read me file. You can also visit out main website as 
http://www.aisangam.com/
