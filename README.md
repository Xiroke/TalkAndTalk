# TalkAndTalk
django project

## How to use

```sh
git clone https://github.com/Xiroke/TalkAndTalk.git
```

ACTIVATE VENV

On windows
```sh
python -m venv venv
.venv\Scripts\activate
```

On Linux
```sh
mkvirtualenv --python=/usr/bin/python3.10 mysite-virtualenv
source mysite-virtualenv/bin/activate
```

create file ".env" in folder "TalkAndTalk"
and add SEKRET_KEY
example
```sh
SECRET_KEY = "django-insecure-w)34&c$g%edfsdgrk-0(q7j&fub!fdsf2%23423554nua%l97a3qpm^hm_#"
```

```sh
cd TalkAndTalk
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
python manage.py runserver
```
