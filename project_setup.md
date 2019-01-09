This is a guide to install and run the ayouto project on your local machine

Setup Database:

- Install PostgresSQL (Google it :) )
- Create a database
- Create a admin user to access to db
- Create environment variables for db_name, db_user, db_password

Setup Email backend:

- Receive email password from project manager, and create a smtp_key environment variable for it


Setup Python Environment

- Install python3 and pip3
- Create virtual environment and activate it (optional)
- Install packages from the requirements.txt

Setup Project

- Clone the git repo
- Go to django root folder (folder containing manage.py)
- Run: 
```
python manage.py makemigrations
python manage.py migrate
```

After this your db should be up to sync. You do not have to run these commands unless there is a change in DB schema

- Run below command to create an admin user for the project and input the required information:
```
python manage.py createsuperuser

```

- Run below command to start the server:
```
python manage.py runserver 
```

- Login to admin panel by going to 'server_domain'/admin
- Go to the Auth/Groups panel and create following groups:
    * manufacturer
    * customer
    * seller
   
You are good to go, and can run the project without any problem
If you encounter any problem please first address google, and then the project manager