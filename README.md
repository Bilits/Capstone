# CryptoSim Project Installation

Here are step by step instructions for running the project successfully:

## Installation

Download the repository:

```bash
$ git clone https://github.com/Bilits/Capstone.git
```
Create a virtual environment and Install requirements:
(in case your python3 package does not contain
virtualenv run the following command: $ pip install virtualenv)
```python
$ cd cryptosim
$ python3 -m virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
After that, run the migration:
```bash
$ python manage.py makemigration
$ python manage.py migrate
```
To create the super user for the admin panel run the following and choose your
username and password:
```bash
$ python manage.py createsuperuser
```
After all these steps, you should have a working project. Try to run:
```bash
$ python manage.py runserver
```
You can now check:
```bash
http://127.0.0.1:8000/
Admin panel: http://127.0.0.1:8000/admin
```
You can now try to register regular user at http://127.0.0.1:8000/register and after the
email confirmation you can login at http://127.0.0.1:8000/login and see the dashboard.

## Contributing
Please let us know if you ran into any issue during the installation

Please make sure to register users/admins as appropriate.
