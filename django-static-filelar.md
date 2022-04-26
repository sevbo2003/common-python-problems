## Djangoda static filelarning ishlamaslik muammosi
***
#### Assalomu alekum. Ushbu maqolada static filelarning ishlamaslik muammosini bartaraf etamiz.
Ushbu maqolaning namunamiy kodlarini [ushbu sahifa](https://github.com/sevbo2003/common-python-problems/tree/master/django-static-filelar) dan topishiz mumkin. Qani unda boshladik
***
Demak maqolani 2 qismga bo'lamiz [**Local**](https://github.com/sevbo2003/common-python-problems/blob/master/django-static-filelar.md#local) va [**Production**](https://github.com/sevbo2003/common-python-problems/blob/master/django-static-filelar.md#production). Ya'ni static filelarning local serverimizda va **deploy** qigandan keyingi ishlamaslik sabablarini ko'rib chiqamiz.

## Local
Demak birinchi django projectimizda static filelarni qanday sozlash kerakligini bir nechta bosqichlarda ko'rib chiqamiz.

1. **Static ni `settings.py url.py` qo'shish** 
   1. `settings.py` file ichiga `STATIC_URL` ni qo'shish kerak. Masalan: `STATIC_URL = 'static/'`
   2. `STATIC_ROOT` yoki `STATICFILES_DIRS` ni larni `STATIC_URL` qo'shish kerak. Bu ikkalasini farqi nimada? Qisqa qilib aytgan `STATICFILES_DIRS` `DEBUG=True` bo'lgan paytda, `STATIC_ROOT` esa `DEBUG=False` bo'lgan paytda ishlaydi. Masalan:
       ```
      STATIC_URL = 'static/'
      if DEBUG == True:
          STATICFILES_DIRS = (BASE_DIR / 'static',)
       else:
          STATIC_ROOT = BASE_DIR / 'static_root'
      ```
        Bu yerda menda static va static_root degan papkalar asosiy directory da joylashganligi uchun `BASE_DIR` qildim va `DEBUG=True` bo'lganda `STATICFILES_DIRS` ni, aks holda `STATIC_ROOT` ni ishlat deb shart berdik
   3. Asosiy `urls.py` ni ichiga static url larni tanitishimiz kerak. Buning uchun `urlpatterns` ga `STATIC_URL` va `STATICFILES_DIRS` ni qo'shib qo'yamiz. Namunaviy kod:
      ```
         from django.conf import settings  # setting.py ni import qildik
         from django.conf.urls.static import static
   
         urlpatterns = [
             path("admin/", admin.site.urls),
         ]

         urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
         
      ```
   Mana barchasini sozlab oldik endi keyingi qiladigan ishimiz `template`da static filelarni to'g'ri ko'rsatish

2. **Static ni `templatelarda` ishlatish** 
   1. Har doim `{% load static %}` ni html file ling eng yuqorisiga agar `{% extends 'base.html' %}` bo'lsa undan pastiga qo'shib qo'ying.
   2. Endi esa qanday static file ni to'g'ri ko'rsatishni ko'rib o'tamiz. Odatda static filedan quyidagi holatda ma'lumot olinadi: 
    
      ```<img src="./rasmlar/rasm.png'" alt="">```
      
      Biz esa buni quyidagi holatga ko'chirishimiz kerak 
      
      ```<img src="{% static 'images/right-arrow.png' %}" alt="">``` **Mana endi static filelar ishlaydi**

## Production
#### Endi esa Django project ni deploy qigandan keyin ishlamaslik holatlarini ko'rib chiqamiz.
Agar `DEBUG=False` qildizmi szning static filelaringiz ishlamaydi. Buning asosiy sababi esa endi django szning static filelarizni saqlamaydi. Chunki siz production leveldasiz va static filelarni server da saqlashiz kerak. Masalan `whitenoise` yoki `NGINX`. 
   1. Eng asosiysi `STATIC_ROOT` borligiga ishinch hosil qiling. Undan keyin esa `python manage.py collectstatic`  buyrug'ini bering.
   2. Keyingi bosqich esa *static* filelarizni saqlamoqchi bo'gan serverlarizning sozlamalarini sozlab chiqish. Bular siz qaysi server ni ishlatayotganizga bog'liq
#### Agarda DEBUG=False qilgan holatda local serverizda static filelarni ishlashini xohlasayiz *1-bosqich* ni bajaring va keyin `python manage.py runserver --insecure` buyrug'i orqali ishlating


## So'ngi so'zi
Agar maqola yoqqan bo'lsa telegram kanalimizga a'zi bo'ling [malikovdev](https://t.me/malikovdev)
Xato kamchiliklar bo'lsa tuzatib Pull Request bersangiz xursand bo'lamiz. **Rahmat**
