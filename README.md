# gazzetta

- Posts
- Categories
- Search
- Tags
- Registration and Authentication

_ _ _ _ _ _ _ _ _ _ _

### Build with
* Django 4.1.5
* Bootstrap 5
* Postgres 14

_ _ _ _ _ _ _ _ _ _ _

### Installation

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


5. Create '.env' file in settings root and paste this:

 ```
   root=true
 
   SECRET_KEY=password from Djescrety

   DB_NAME=your_db_name_created

   DB_USER=your_db_user

   DB_PASSWORD=your_password

   DB_HOST=localhost

   DB_PORT=5432
   ```
