# Overview

Vault is a manager of passwords, notes, addresses, payment cards and bank accounts, as well as having a strong password generator.

Vault's goal is to solve the problem of password, notes, calendars, cards and accounts fatigue, centralizing the management of these objects. Objects are synced to any other supported browsers, the main ones being Chrome, Edge and Mozilla Firefox.

# Distinctiveness and Complexity

Vault is different enough from the other projects in this course because Vault is not a browser, a wiki, a social network, an email website, or an e-commerce website, it is literally a personal vault where a user can manage your passwords, personal notes, addresses, payment cards and bank accounts.

Vault is more complex than those because it is built by implementing every concept and technique learned during the course, some of these are:

- HTML and CSS are implemented in this website to create and design different templates and implement the mobile responsive requirement.
- Git was used to track every change and version made during the development process and to push the project.
- Python and its Django framework were used to implement the backend of this project.
- JavaScript was used to provide an intuitive user interface and also to communicate with the Google Recaptcha V3 API on the login page to verify users.
- Scalability and Security. I developed this project using a modular architecture that allows my project to be more secure, scalable and easy to maintain. Each module is an application that together forms the complete project.

Additionally, Vault implement reCAPTCHA v3 Google API to protect itself from fraudulent activities, spam and abuse, which make Vault a secure site.

Vault also was developed using an advanced Django concept like Class Based Views and Mixins which makes the code easier to understand and write.


# Files content

The files structure is as follows:

```
- passwords/
    - admin.py
    - apps.py
    - models.py
    - tests.py
    - urls.py
    - utils.py
    - views.py 

- project5/
    - asgi.py
    - mixins.py
    - settings.py
    - urls.py
    - wsgi.py

- static/
    - assets/
        - css/
            - styles.css
    - img/
        - add-icon-hovered.png
        - add-icon.png
        - address.png
        - bank-account.png
        - note.png
        - password.png
        - payment_card.png
    - capstone.css
    - capstones.js
    - toggle_add_icon.js

- templates/
    - partials/
        - nav.html
    - password/
        - generate_password.html
    - users/
        - account.html
        - sign_in.html
        - sign_up.html
    - vault/
        - addresses.html
        - all-items.html
        - bank_accounts.html
        - create_item.html
        - delete_item.html
        - detail_item.html
        - notes.html
        - passwords.html
        - payment_cards.html
    base.html

- users/
    - admin.py
    - apps.py
    - models.py
    - tests.py
    - urls.py
    - utils.py
    - views.py

- vault/
    - admin.py
    - apps.py
    - models.py
    - tests.py
    - urls.py
    - utils.py
    - views.py

- db.sqlite3
- manage.py
- README.md
- requirements.txt
```

## **Backend files**

### **Models**

There are 6 models that Vualt use to store data:

    1. User - A fully featured User model with admin-compliant permissions.
    2. Password - Holds information for created passwords.
    3. Note - Holds information for created notes.
    4. Address - Holds information for created addresses.
    5. PaymentCard - Holds information for created payment cards.
    6. BankAccount - Holds information for created bank accounts.

### **Views files**
'views.py' contains the class based views for the web application. These views sends and receives http requests and responses. They also deal with model instances and querysets.

### **manage.py file**
This file is used as a command-line utility and for deploying, debugging, or running the web application.This file contains code for runserver, makemigrations or migrations, etc. that we use in the shell. (Not changing anything here).

### **__init__.py files**
This file is empty and remains that way. they are present only to tell that this particular directory is a package. (No changes to this file either).

### **settings.py**
This file is present for adding all thr applications and the middleware application present. This also has informations about templates and databases. This is present in the main file of the Django web application.

### **urls.py files**
This file handles all the URLs of our Django web application. This file contains the lists of all the endpoints that we will have for our web application. Also, this files is like a link to the views in the app with the host web URL.

### **wsgi folder**
This file mainly concerns with the WSGI server and is used for deploying the web application on to the servers similar to apache, etc. (No changes to this file as well)

### **admin.py files**
Similar to the name of the file, this file is used for registering the models into the django administration. The models that are present have a superuser/admin who can control the information that is being stored. (they are pre-built)

### **apps.py files**
This file deals with the application configuration of the apps. The default configuration is sufficient enough in most of the cases.

### **models.py files**
This file contains the models of our web application (classes). They are the blueprints of the database we are using and hence contain the information regarding attributes and the fields, etc of the database.

### **test.py files**
This file containts the code that contains different test cases for the application. It is used to test the working of the application. (did not implement tests in this web application)

## **Frontend files**

### **templates/base.html**
This file is the parent HTML file. This file contains the main structure of the web site and also link HTML files with static files like JS files and CSS files.

### **templates/partials/nav.html**
This file contains HTML code for the navbar.

### **templates/password/generate_password.html**
This file contains HTML code for the main page of the Password app. Displays a form to generate a secure password.

### **templates/users/account.html**
This file contains HTML code for the account page. Displays user's account information.

### **templates/users/sign_in.html**
This file contains HTML code for the login page. Displays a login form.

### **templates/users/sign_up.html**
This file contains HTML code for the sign up page. Displays a register form.

### **templates/vault/addresses.html**
Shows the addresses created as cards.

### **templates/vault/all-items.html**
Shows all the items created as cards.

### **templates/vault/bank_accounts.html**
Shows the bank accounts created as cards.

### **templates/vault/create_item.html**
Shows the corresponding form to create an item (password, note, address, etc).

### **templates/vault/delete_item.html**
Shows a question for the user to confirm an item delete.

### **templates/vault/detail_item.html**       
Shows the detailed information about a specific item.

### **templates/vault/notes.html**
Shows the notes created as cards.

### **templates/vault/passwords.html**
Shows the passwords created as cards.

### **templates/vault/payment_cards.html**
Shows the payment cards created as cards.

### **static/capstone.css**
Contains styles for HTML elements in tmeplates

### **static/assets/css/styles.css**
Contains styles for "a" elements, this is a Bootstrap Studio files and its content can be put in static/capstone.css file.

### **static/capstone.js**
This is the main JS file for the Vault project. It contains functions and event listeners that deal with handling the user's interaction with the website and thus create a dynamic website.

# How to run Vault
Once you are placed in the project directory in the terminal, execute the following command to install the requirements
```
pip install requirements.txt
```

Once  you have installed all the requirements in requirements.txt, run the following commands to create the SQLite database
```
python manage.py makemigrations
python manage.py migrate
```

Finally, run the app with:
```
python manage.py runserver
```




# Additional information

There is no additional information for this project.