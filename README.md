## Overview

REST API for Resturant-Self-Order.

## Project Setup

Follow the steps below to set up the project on your environment. If you run into any problems, feel free to leave a 
GitHub Issue or reach out to any of our communities above.

Clone the repo:
```shell
git clone https://github.com/Restaurants-Self-Order/Backend.git
```

Install required packages:
```shell
pip3 install -r requirements.txt
```

Copy the folders `djangorestframework_simplejwt-4.6.0.dist-info`, `djoser`, `djoser-2.1.0.dist-info`and `rest_framework_simplejwt` that are inside `v1/third_party/` to your environment install path.

Rename the `.env.example` file to `.env` and put your email and app password to the fields to send emails.

Run Migrations:
```shell
python manage.py migrate
```

Create SuperUser:
```shell
python manage.py createsuperuser
```