##simpleBBS
A simple BBS which let you publish articles and add comments for the articles and comments, and it also enables web chat: You can chat with others through the web, like web qq.


##Prerequisites
Before you run the program, make sure your server which will run this program has been installed python3, Django, and Pillow module.

How to install the modules? We can use pip to install them easily. Take Ubuntu 14.04 OS for example.
Ubuntu 14.04 installed python3.4 by default. Check your current os's python3 version: 
```
$python3 -V
```

Install the modules:
```
$sudo apt-get install python3-pip
$sudo apt-get install python-dev
$sudo pip3 install django
$sudo apt-get install libjpeg8-dev
$sudo pip3 install pillow
```

Refer the Django installation doc for more details: https://docs.djangoproject.com/en/dev/topics/install/

Refer the Pillow installation doc for more details: http://pillow.readthedocs.io/en/3.0.x/installation.html

We use Django 1.9.5 for the project.


##Clone the project
```
$sudo apt-get install git
$cd /tmp
$sudo git clone https://github.com/joey100/simpleBBS.git
```


##Start the project 
```
$cd /tmp/simpleBBS
$sudo python3 manage.py runserver 127.0.0.1:8000
```

Then open URL http://127.0.0.1:8000/bbs/ , you will see some test articles are already there. You can use alex/alex12345 or eric/eric12345 to login, then you can add new articles and comments. You can also chat with other users through the web.

URL http://127.0.0.1:8000/admin/ is for administration.


Use below command to create a new admin user.
```
$sudo python3 manage.py createsuperuser
```



##Known issues
- When you chat with other users, in the message input window, if you press Enter, then the message will be sent out immediately. Do not click the send message button in the right, it's useless.
- If your Ubuntu OS doesn't install xfce or Gnome Desktop, then you should replace 127.0.0.1 to be the Ubuntu OS Nic ip address in other OS's URL.