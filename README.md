## Django Rest Framework Group Based Permission - rbac


1. Install all the requirements
`pip install -r requirements.txt`
2. Make migrattions
 `python manage.py makemigrations`
3. Migrate the migrations
`python manage.py migrate`
4. Run group.py
`python group.py`
5. Create superuser provide groups.id: 1 (group id of admin)
`python manage.py createsuperuser`
6. Run server
`python manage.py runserver`

- Two groups
Admin
Ensurer

- Admin group user can

Login
Add a new user
List all users
View individual user
Delete users
Update all users

Ensurer group user can

Login
List all users
View and Update own detail
Without login, no user can get access to the system.