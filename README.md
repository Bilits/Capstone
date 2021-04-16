CryptoSim Project Installation<br />
Here are step by step instructions for running the project successfully:<br />
• Download the repository:
o $ git clone https://github.com/Bilits/Capstone.git
• Create a virtual environment and Install requirements:
o $ cd cryptosim
o $ python3 -m virtualenv venv (in case your python3 package does not contain
virtualenv run the following command: $ pip install virtualenv)<br />
o $ source venv/bin/activate
o $ pip install -r requirements.txt
• After that, run the migration:
o $ python manage.py makemigrations
o $ python manage.py migrate
• To create the super user for the admin panel run the following and choose your
username and password:<br />
o $ python manage.py createsuperuser
• After all these steps, you should have a working project. Try to run:<br />
o $ python manage.py runserver
• You can now check:<br />
o http://127.0.0.1:8000/
o Admin panel: http://127.0.0.1:8000/admin
• You can now try to register regular user at http://127.0.0.1:8000/register and after the<br />
email confirmation you can login at http://127.0.0.1:8000/login and see the dashboard.<br />
Please let us know if you ran into any issue during the installation<br />