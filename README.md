# gazzetta

- Posts
- Categories
- Tags
- Registration and Authentication

# Requirements

* Python 3.9 and up

# Installation 

1. Create virtual environment:

```
python -m venv venv
```

2. Activate virtual environment
```
.\venv\Scripts\activate
```

3. Install requirements

```
python -m pip install -r requirements.txt
```

4. Create Postgres database.

5. Go to [Djescrety](https://djecrety.ir/) generate secret key and copy it.


6. Create '.env' file in settings root and paste this:

   root=true
 
   SECRET_KEY=password from Djescrety

   DB_NAME=your_db_name_created

   DB_USER=your_db_user

   DB_PASSWORD=your_password

   DB_HOST=localhost

   DB_PORT=5432

7. Run

```
python manage.py makemigrations
```
8.Run

```
python manage.py migrate
```
9. Run

```
python manage.py runserver
```


# Build with
* Django 4.1.5
* Bootstrap 5
* Postgres 14
