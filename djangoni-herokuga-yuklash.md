## **Django loyihani herokuga yuklash bo'yicha qo'llanma**
***

> Django loyihani herokuga yuklash bo'yicha qo'llanma Ushbu maqolada djangoni herokuga terminal orqali yuklash ketma-ket liklarini ko'rib chiqamiz

> Muallif: [Abdusamad](https://t.me/malikovdev)

> Savollar uchun guruh: [Djangouzb](https://t.me/djangouzb)

Bo'limlar   
 1. [Django qismi]()
 2. [Database qismi]()
 3. [Heroku qismi]()
 4. [Deploy vaqti uchraydigan muammolar]()


## Django qismi
***
> ⚠️ Virtual muhit ichida ekanligizga ishonch hosil qiling
1. Kreakli packege larni o'rnatib olamiz
    - gunicorn (application server [batafsil](https://vsupalov.com/what-is-gunicorn/)
    - dj-database-url (Database uchun)
    - whitenoise (static filelarni saqlash uchun [batafsil](https://github.com/sevbo2003/common-python-problems/blob/master/django-static-filelar.md)
    - psycopg2 (Postgres database uchun)

    ```pip install gunicorn dj-database-url whitenoise psycopg2-binary```

2.  ```pip freeze > requirements.txt```  -> bu o'rnatilgan dasturlarni herokuga tanitadi va heroku shundagi package larni o'rnatadi

3. `python3 --version`  
    Chiqqan versiyani runtime.txt fayli ichiga yozamiz yoki quyidagi kommandani tering
    
    ```echo "python-3.10.4" > runtime.txt```

    python versiyasi o'zniga o'zizni python versiyayizni yozing
4. ```echo "web: gunicorn PROJECT_NOMI.wsgi" > Procfile```
    
    Bu yerda `PROJECT_NOMI` o'rniga wsgi.py fayli turgan papkani yozing.
5. ```
    INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
     # ...
    ]
    ```
    whitenoise static filelarni saqlashi uchun installed apps ichiga qo'shishimiz kerak
6. ``` 
    ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
    ```
7. ` DEBUG = False`
8. ```
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        
        # whitenoise ni shu yerga qo'shing
        'whitenoise.middleware.WhiteNoiseMiddleware',
        # ...
    ]
    ```
    > Bu yerda sal e'tiborli bo'ling. Ya'ni whitenoise ni Djangoning o'zida mavjud bo'lgan `SecurityMiddleware` tagiga qo'shing
9. Bu qismini bajarishdan oldin [DATABASE]() qismini ko'rib chiqing va unda qanday database ochishni o'rganasz 
    
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'DATABASE NOMI',
            'USER': 'USER',
            'PASSWORD': "PAROL",
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
        

    import dj_database_url
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
    ```
    Shularni `sqLite3` database o'rniga qo'shib qo'ying

10. ```
    STATIC_ROOT = BASE_DIR / 'static'

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    ```
    Bu static filelarning ishlashi uchun. Static filelarhaqida batafsil [bu yerda](https://github.comsevbo2003/common-python-problems/blob/masterdjango-static-filelar.md) o'qishiz mumkin.
    ### Bu django qismining yakuni.


## Database qismi
 1. Agar windows ishlatsangiz PostgreSQL terminaliga kiring. [Qanday kirish haqida](https://linuxhint.com/connect-to-postgresql-database-command-line-windows/). 
 Agar **Linux** foydalanuvchisi bo'lsangiz `sudo -u postgres psql` buyrug'ini berish yetarli.
 2. Quyidagi buyruqlarni **ketma-ketlikda** bajaring.
    - `create database dbnomi;`
    - `create user dbuser with encrypted password 'parol123';`
    - `grant all privileges on database dbnomi to dbuser;`
    
    Ushbu buyruqlarni terganizdan keyin `GRANTED` deb tasdiqlaydi
 3. Keyin shu Database nomi useri va parolini django loyihayiz ichidagi DATABASE ichiga kiritasz

## Heroku qismi
 1. Agar heroku akkauntingiz bo'lmasa [ushbu yerdan](https://signup.heroku.com/) yangi ochishingiz kerak bo'ladi. Agar bo'lsa shu akkauntingizga brauzer orqali kirib qo'ying
 2. **Heroku-CLI** o'rnatilgan bo'lishi kerak komputeringizda. Agar bo'lmasa pastdagilardan birini bajarib o'rnatib oling.
    - Mac uchun: `brew install heroku/brew/heroku`
    - Linux uchun snap orqali: `sudo snap install heroku --classic`
    - Windows uchun: [Ushbu sahifa](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) orqali yuklab oling
 3. O'rnatib olganizdan so'ng Heroku akkountga uchbu buyruq      orqali kiring: **Brauzer** ochiladi va o'sha orqali kirasz
    ```
    heroku login
    ```
    
4. Herokuda loyihayiz uchun app yaratish
    ```
    heroku create proyekt_nomi
    ```
    
5. Endi django loyihayiz turgan papkada turganiz ga ishonch hosil qiling va ushbu buyruqlar orqali heroku ga yuklaysiz loyihayizni:
    ```
    git add -A
    git commit -am "Initial"
    git push heroku master
    ```
    Mana endi sizning loyihangiz Herokuga yuklandi. Endi navbat keyingi bosqichga ))
6. PostgreSQL ishlashi uchun uni Herokuda aktivlashtirish kerak. Quiyidagi buyruqni tering:
    ```
    heroku addons:create heroku-postgresql:hobby-dev --app PROYEKT_NOMI
    ```
    Bu yerda **PROYEKT_NOMI** o'rniga boshida heroku uchun yaratgan PROYEKT_NOMI ni yozing
7. Endi navbat django uchun har doim ishlatadigan buyruqlarga. Menimcha hammasini bilasz 😊:
    ```
    heroku run python manage.py collectstatic

    heroku run python manage.py makemigrations

    heroku run python manage.py migrate

    heroku run python manage.py createsuperuser

    heroku open # brauzerni ochadi.

    ```

## Muammolar
 1. `heroku run python manage.py collectstatic` qilganda chiqadigan error. Ushbu ketma-ketliklarni bajaring:
    - ``` heroku config:set DISABLE_COLLECTSTATIC=1 ```
    - ``` git push heroku master ```
    - ``` heroku run python manage.py collectstatic ```