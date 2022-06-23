## 🔗 Links

[![portfolio](https://img.shields.io/badge/my_portfolio-1dcf57?style=for-the-badge&logo=ko-fi&logoColor=white)](https://amrit-giri.com.np/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/amrit-giri-6a2500198/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/AmritGi56713133)
[![YouTube](https://img.shields.io/badge/youtube-ffffff?style=for-the-badge&logo=youtube&logoColor=red)](https://m.youtube.com/channel/UCVme0WEkXsjIUJXMQPx_iHA?sub_confirmation=1)
[![GitHub](https://img.shields.io/badge/github-ffffff?style=for-the-badge&logo=github&logoColor=black)](https://github.com/Amrit-Giri/)


# LeSp_E-Stores
This is Online Electronic shopping store. Responsive Online Shopping Store Using Django, HTML, CSS, JavaScript, Bootstrap framework etc.

# Projects Live Demo
https://lespstore.pythonanywhere.com/

# Used in Projets
`HTML` `CSS` `JavaScript` `Bootstrap` `Ajax` `Jquery` `Django` `Python` `FontAwesome` `Owl Carosul`

# How does a virtual environment work?

We use a module named virtualenv which is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

# Installing virtualenv
$ `pip install virtualenv`
# Test your installation:
$ `virtualenv --version`
# Using virtualenv
You can create a virtualenv using the following command:

$ `virtualenv my_name` 	

if above this☝️ command is not working tyr this↙️ command.

$ `python -m virtualenv my_name`

After running this command, a directory named my_name will be created. This is the directory which contains all the necessary executables to use the packages that a Python project would need. This is where Python packages will be installed.

If you want to specify Python interpreter of your choice, for example Python 3, it can be done using the following command:

$ `virtualenv -p /usr/bin/python3 virtualenv_name`

To create a Python 2.7 virtual environment, use the following command:

$ `virtualenv -p /usr/bin/python2.7 virtualenv_name`

Now after creating virtual environment, you need to activate it. Remember to activate the relevant virtual environment every time you work on the project. This can be done using the following command:

$ `source virtualenv_name/bin/activate`

![image](https://user-images.githubusercontent.com/85377404/169666037-24f28de7-9029-45cb-8c2b-c7c55cee8c12.png)

Once the virtual environment is activated, the name of your virtual environment will appear on left side of terminal. This will let you know that the virtual environment is currently active. In the image below, venv named virtual environment is active.

Now you can install dependencies related to the project in this virtual environment. For example if you are using Django 1.9 for a project, you can install it like you install other packages.

![image](https://user-images.githubusercontent.com/85377404/169666065-9fb5f5fe-e720-4921-bbb5-28262875dc05.png)

`(virtualenv_name)$ pip install Django==1.9`

The Django 1.9 package will be placed in virtualenv_name folder and will be isolated from the complete system.

Once you are done with the work, you can deactivate the virtual environment by the following command:
`(virtualenv_name)$ deactivate`

![image](https://user-images.githubusercontent.com/85377404/169666096-aebd8ee4-d600-4f49-8dac-897b88ab9295.png)

Now you will be back to system’s default Python installation.

# Command

$ `django-admin` --> Show details use in Django

$ `pip freeze` --> Show install  packages on Django.

$ `django-admin startproject <project_name> ` --> Create Project in Django.

$ `cd <project_name>` --> Change Directory and go to project folder.

$ `python3 manage.py runserver ` --> Start Django project port:8000 `http://127.0.0.1:8000`

$ `python3 manage.py runserver <port_no>` --> If you want to change your project server port's  then Run this commsnds.
##### For Example:
$ `python3 manage.py runserver 8080`

# How to migrate Default migrations
$ `python manage.py makemigrations`

$ `python manage.py migrate`

# Create Superuser in Django
$ `python manage.py createsuperuser` --> This command id Created Django Admin User.

Username: <input type="text" placeholder="Username"/>

Email address: <input type="email" placeholder="Username"/>

Password: <input type="password" placeholder="Username"/>

Password(again): <input type="password" placeholder="Username"/>

# Requirments install
$ `pip install -r <file_name> `

$ `pip install django`

$ `pip install django-pillow`

$ `pip install django-jazzmin`

$ `pip install django-tinymce`

$ `pip install django-form-dynamic`



# ProjectScreenShot 

## Home
![image](https://user-images.githubusercontent.com/85377404/169668675-40e42e09-898b-4f85-b806-91ac1205c51d.png)

![image](https://user-images.githubusercontent.com/85377404/169668683-73a2044f-ad52-48d8-b4f4-b48d329e4265.png)

![image](https://user-images.githubusercontent.com/85377404/169668691-63d8d07f-7044-4ca2-a37d-c83580f9764d.png)

## Mobile

![image](https://user-images.githubusercontent.com/85377404/169668658-fb92867f-085f-4555-8d15-5b4478ca4258.png)

![image](https://user-images.githubusercontent.com/85377404/169668740-79e6b01a-98b0-47c2-9e07-d6b7bf16dc3c.png)

## Laptops
![image](https://user-images.githubusercontent.com/85377404/169668745-abe317be-5c68-49ee-a406-4b49da8b0e10.png)

![image](https://user-images.githubusercontent.com/85377404/169668795-d2f1c649-0dd2-4a68-80d6-c275a1171742.png)

## Profile
![image](https://user-images.githubusercontent.com/85377404/169668812-691d7339-1832-429d-ba1a-98d5759c3501.png)

## Address
![image](https://user-images.githubusercontent.com/85377404/169668836-c932e2bf-4f31-4ba6-9ed4-580c37daa8fa.png)

## Order
![image](https://user-images.githubusercontent.com/85377404/169668848-e371d80c-94e6-48ca-91a3-fe6d50edc9ef.png)

## Password Change
![image](https://user-images.githubusercontent.com/85377404/169668856-30353c2d-aa11-493a-a98a-6938e45ca6ac.png)

## Shopping Cart
![image](https://user-images.githubusercontent.com/85377404/169668874-78ac914f-1840-4f3a-9fa8-c3c122de04e4.png)

## Order Summary
![image](https://user-images.githubusercontent.com/85377404/169668880-c5bbd4d4-fb25-4bc6-b86d-40489a3b2f16.png)

## Registration
![image](https://user-images.githubusercontent.com/85377404/169668882-7e7000bb-ee9d-401b-abdb-91624935b596.png)

## Login
![image](https://user-images.githubusercontent.com/85377404/169668891-0a7146fa-e3c0-444a-b8c8-2d30b6400163.png)

## Reset Password
![image](https://user-images.githubusercontent.com/85377404/169668901-b7646929-bfa2-4f4f-b0ff-900bdafd0da0.png)

# Admin Pannel ScreenShote

## Dashboard
![image](https://user-images.githubusercontent.com/85377404/169668925-ab8adce5-13dc-4bf6-bd49-afb31c69f65e.png)

## Carts
![image](https://user-images.githubusercontent.com/85377404/169668943-1a0c71b1-0225-4463-8683-d6161f684e7c.png)

## Customers
![image](https://user-images.githubusercontent.com/85377404/169668948-eed438be-df82-432d-bceb-5b00c5b91135.png)

## Order Placeds
![image](https://user-images.githubusercontent.com/85377404/169668960-570be13f-b196-4397-add5-970bd865c293.png)

## Products
![image](https://user-images.githubusercontent.com/85377404/169668969-c414727a-2403-4e6d-b7e9-1948f88b26c0.png)

## Users
![image](https://user-images.githubusercontent.com/85377404/169669081-72a8120b-b56e-4d51-9a15-3abe6f04ca85.png)

## Products
![image](https://user-images.githubusercontent.com/85377404/169669092-6d462169-2f61-4425-bdcd-1832095db16a.png)


