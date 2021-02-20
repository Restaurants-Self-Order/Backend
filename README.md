## Overview

REST API for Resturant-Self-Order.

## Project Setup

Follow the steps below to set up the project on your environment. If you run into any problems, feel free to leave a 
GitHub Issue or reach out @Hussu or @Sazid Ahmed on slack.

Activate Your Virtual Environment.

Clone the repo:
```shell
git clone https://github.com/Restaurants-Self-Order/Backend.git
```

Install required packages:
```shell
pip3 install -r requirements.txt
```

Copy the folders `djangorestframework_simplejwt-4.6.0.dist-info`, `djoser`, `djoser-2.1.0.dist-info`and `rest_framework_simplejwt` that are inside `v1/third_party/` to your environment install path. Windows: `\{{your_env}}\Lib\site-packages` and Linux/MacOS: `{{your_env}}/lib/{{pythonX.X}}/site-packages`

Rename the `.env.example` file to `.env` and put your email and app password to the fields to send emails.

Run Migrations:
```shell
python manage.py migrate
```

Create SuperUser:
```shell
python manage.py createsuperuser
```

## API Documentation
### Login
url: http://yahyarestaurant.pythonanywhere.com/auth/jwt/create/

method: post

body: email, password

### SignUp
url: http://yahyarestaurant.pythonanywhere.com/auth/users/

method: post

body: email, password, re_password

## User Activate
url: http://yahyarestaurant.pythonanywhere.com/auth/users/activation/

method: post

body: uid, token (gets sent to the users email address)

### Partner Add
url: http://yahyarestaurant.pythonanywhere.com/partner

method: post

body: name, street_address, city, first_name, last_name, email, phone, country

### Partner List
url: http://yahyarestaurant.pythonanywhere.com/partner

method: get

condition: needs to be a staff account to have permission

### Partner Details
url: http://yahyarestaurant.pythonanywhere.com/partner/{uuid}

method: get

condition: needs to be a staff account to have permission

### Partner Patch
url: http://yahyarestaurant.pythonanywhere.com/partner/{uuid}

method: patch

condition: needs to be a staff account to have permission

body: name, street_address, city, first_name, last_name, email, phone, country, status (not all fields required)

### Partner Post
url: http://yahyarestaurant.pythonanywhere.com/partner/{uuid}

method: post

condition: needs to be a staff account to have permission

body: name, street_address, city, first_name, last_name, email, phone, country, status (all fields required)

### Partner Delete
url: http://yahyarestaurant.pythonanywhere.com/partner/{uuid}

method: delete

condition: needs to be a staff account to have permission