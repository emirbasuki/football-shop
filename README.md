**Tugas 2**
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


**Tugas 3**
1. **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data delivery diperlukan karena:
- Memungkinkan pertukaran informasi antara client dan server
- Mendukung integrasi antar sistem yang berbeda
- Memfasilitasi komunikasi asynchronous
- Memungkinkan format data yang fleksibel (JSON, XML, dll)
- Mendukung skalabilitas platform dengan memisahkan frontend dan backend

2. **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
- Sintaks lebih sederhana - JSON menggunakan format key-value yang mudah dibaca
- Ukuran file lebih kecil - Tidak memerlukan closing tags seperti XML
- Parsing lebih cepat - Struktur data yang lebih sederhana
- Native JavaScript support - JSON adalah subset dari JavaScript
- Mudah dikonversi - Dapat dengan mudah diubah ke object pada berbagai bahasa pemrograman

3. **Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
is_valid() berfungsi untuk:
- Memvalidasi data yang diinput user sesuai dengan rules yang didefinisikan
- Mencegah data invalid masuk ke database
- Memberikan feedback ke user jika ada kesalahan input
- Mengkonversi data input ke format yang sesuai dengan model

4. **Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
CSRF token diperlukan karena:
- Mencegah Cross-Site Request Forgery (CSRF) attacks
- Memastikan form berasal dari sumber yang legitimate
- Melindungi user dari aksi yang tidak diinginkan
Tanpa CSRF token:
- Penyerang bisa membuat form palsu yang meniru form asli
- Bisa mengeksploitasi session user yang sedang login
- Dapat melakukan aksi tanpa sepengetahuan user (seperti transfer dana, mengubah password)
Contoh eksploitasi:
- User login ke website bank
- Penyerang mengirim link berbahaya
- User mengklik link tersebut
- Form palsu mengirim request transfer tanpa sepengetahuan user

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
menambahkan fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id pada main/views.py

Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
pada main/urls.py, tambahkan from main.views import show_xml, show_json, show_xml_by_id, show_json_by_id
dan tambahkan path pada urlpatterns
...
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
...

- Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
membuat html create product pada main/templates/create_product.html untuk add product dan detail pada main/templates/main.html yang akan diarahkan ke product_detail.html 


- Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
menambahkan field yang ingin ditambahkan pada main/forms.py
fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "stock", "brand", "size"]

- Membuat halaman yang menampilkan detail dari setiap data objek model.
membuat product-details pada main/product_detail.html untuk menampilkan info pada halaman web

6. **Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**
sudah lengkap informasinya

7. **Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**
