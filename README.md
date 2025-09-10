Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
https://pbp.cs.ui.ac.id/emir.fadhil41/footballshop

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat Proyek Django
- membuat direktori football-shop
- aktifkan venv : env\Scripts\activate
- membuat proyek Django : django-admin startproject run_station

2. Membuat Aplikasi dengan nama main
- menjalankan perintah : py manage.py startapp main

3. Routing pada proyek untuk aplikasi main
- membuka file run_station/settings.py
- tambah 'main' ke INSTALLED_APPS
- membuka file run_station/urls.py
- tambahkan
from django.urls import path, include
urlpatterns = [
    ...,
    path('', include('main.urls')),
]

4. Membuat model product dengan atribut yang diminta
- membuka main/models.py
- tambahkan name, price, description, thumbnail, category, is_featured, stock, rating, brand, dan size

5. Membuat fungsi pada views.py
- membuka file main/views.py
- menambahkan fungsi untuk merender template :
from django.shortcuts import render
def show_main(request):
    context = {
        'app_name' : 'run station',
        'name': 'Emir Fadhil Basuki',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
- membuat direktori templates di folder main
- membuat main.html di dalam direktori templates :
<h1>Football Shop</h1>

<h4>App:</h4>
<p>{{ app_name }}</p> 
<h4>Name: </h4>
<p>{{ name }}</p> 
<h4>Class: </h4>
<p>{{ class }}</p>

6. Membuat routing pada urls.py aplikasi main
- membuat file main/urls.py
- menulis kode untuk memetakan URL view yang telah dibuat agar dapat diakses melalui browser:
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

7. Melakukan deployment ke PWS
- git add .
- git commit -m "Complete tutorial 2: Implementasi Model-View-Template (MVT) pada Django"
- git push origin master
- git push pws master

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
https://www.figma.com/board/8xd2zUckc1s3iUwFduzYOG/Untitled?node-id=0-1&t=vVIFJc0niQTHtyrx-1

Jelaskan peran settings.py dalam proyek Django!
settings.py berperan sebagai pusat konfigurasi yang mengatur seluruh perilaku proyek Django seperti database, installed apps, middleware, template & static files path, dan konfigurasi keamanan

Bagaimana cara kerja migrasi database di Django?
command : python manage.py makemigrations -> Django membuat file migrasi
command : python manage.py migrate -> Django menerjemahkan file migrasi menjadi perintah SQL untuk membuat/mengubah tabel di database

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Sudah menyediakan banyak fitur bawaan (ORM, auth, admin, panel, dll). Konsep MVC mudah dipahami, mirip pola arsitektur standar yang dipakai di banyak framework lain. Django memiliki struktur proyek yang rapi. Dokumentasi lengkap dan komunitas besar. Django juga cocok untuk fullstack

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
untuk tutorial mudah dipahami dan diikuti sehingga tidak ada masalah.