![image](https://github.com/user-attachments/assets/6fe56cf6-59f4-4ce6-a19d-8de818bab74a)To-Do Ilovasi
Bu Django va PostgreSQL asosida qurilgan kundalik vazifalarni boshqarish ilovasi. Foydalanuvchilar vazifalarni qo'shishi, tahrirlashi, o'chirishi va ularni kategoriyalar bo'yicha filtrlashi mumkin.
Xususiyatlar

Foydalanuvchi autentifikatsiyasi (ro'yxatdan o'tish, kirish, chiqish)
Vazifalarni qo'shish, tahrirlash, belgilash va o'chirish
Vazifalarni qidirish va filtrlash (bugungi, muhim, bajarilgan)
PostgreSQL ma'lumotlar bazasi integratsiyasi
Chiroyli va moslashuvchan interfeys (HTML, CSS)

Texnologiyalar

Backend: Django 4.x, Python 3.8+
Frontend: HTML, CSS
Ma'lumotlar bazasi: PostgreSQL
Vazifalar boshqaruvi: Django ORM

O'rnatish

Repositoriyni klonlang:git clone https://github.com/sizning-username/todo-app.git
cd todo-app


Virtual muhitni yarating va faollashtiring:python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Kerakli paketlarni o'rnating:pip install -r requirements.txt


PostgreSQL'da ma'lumotlar bazasini sozlang va todo_project/settings.py faylida sozlamalarni yangilang.
Migratsiyalarni amalga oshiring:python manage.py makemigrations
python manage.py migrate


Serverni ishga tushiring:python manage.py runserver



Foydalanish

http://127.0.0.1:8000/ manzilida bosh sahifani oching.
Ro'yxatdan o'ting yoki kirish qiling.
Dashboard orqali vazifalarni boshqaring.

Litsenziya
MIT Litsenziyasi ostida tarqatiladi.
Aloqa
Telegram: @https://t.me/Bunyod_Ruziqulov  
