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
<img width="1920" height="1080" alt="Screenshot (55)" src="https://github.com/user-attachments/assets/38d6cbf8-df69-4ea8-996a-afe43faeaa44" />
<img width="1920" height="1080" alt="Screenshot (56)" src="https://github.com/user-attachments/assets/742733cc-c4f5-4cda-95ff-ab03f197e6cb" />
<img width="1920" height="1080" alt="Screenshot (57)" src="https://github.com/user-attachments/assets/0f03efe9-f428-47ff-88c1-ed977691db31" />
<img width="1920" height="1080" alt="Screenshot (58)" src="https://github.com/user-attachments/assets/deb7b62e-2c27-4249-8b41-b1f65e0e6eee" />



**Tugas 4**
1. **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.**
    menambahkan 
    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
    from django.contrib import messages
    from django.contrib.auth import authenticate, login, logout

    tambah fungsi register, login, dan logout
    buat berkas html register dan login pada direktory main/templates

    tambah import dan path register, login, dan logout di main/urls.py

2. **Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.**
    Add user dengan registrasi kemudian login dengan username dan password yang benar

    Pada halaman utama add product sebanyak 3 kali

3. **Menghubungkan model Product dengan User.**
    tambahkan "from django.contrib.auth.models import User" pada main/models.py

    tambah "user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)" pada Product

    jalankan makemigrations dan migrate

    ubah create_product pada main/views.py bagian :
    if form.is_valid() and request.method == 'POST':
            news_entry = form.save(commit = False)
            news_entry.user = request.user
            news_entry.save()
            return redirect('main:show_main')

    modifikasi fungsi show_main
    filter_type = request.GET.get("filter", "all")  # default 'all'

        if filter_type == "all":
            product_list = Product.objects.all()
        else:
            product_list = Product.objects.filter(user=request.user)

        context = {
            'app_name' : 'run station',
            'name': request.user.username,
            'class': 'PBP E',
            'product_list' : product_list,
            'last_login' : request.COOKIES.get('last_login', 'Never')
        }

    tambahkan tombol filter my dan all pada halaman main.html
    <a href="?filter=all">
        <button type="button">All Articles</button>
    </a>
    <a href="?filter=my">
        <button type="button">My Articles</button>
    </a>

4. **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.**
    ini akan menampilkan informasi pengguna (username) :
    pada views.py :
    'name': request.user.username, 

    pada main.html :
    <h4>Name: </h4>
    <p>{{ name }}</p>

    ini akan menampilkan last_login
    pada views.py :
    'last_login' : request.COOKIES.get('last_login', 'Never')

    pada main.html :
    <h5>Sesi terakhir login: {{ last_login }}</h5>

5. **Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).**
    1. **Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.**
    AuthenticationForm adalah form bawaan Django yang disediakan di modul django.contrib.auth.forms.
    Fungsinya untuk melakukan autentikasi pengguna (login). Form ini biasanya digunakan bersama view bawaan LoginView.

    - Karakteristik:
        - Menerima input username dan password.
        - Secara otomatis memvalidasi apakah user ada di database.
        - Mengecek apakah user aktif (is_active=True).
        - Jika validasi lolos, maka data form bisa digunakan untuk login user.

    - Kelebihan:
        - Mudah digunakan, tidak perlu menulis validasi manual.
        - Terintegrasi langsung dengan sistem User bawaan Django.
        - Aman karena otomatis menangani hashing password dan pengecekan status akun.
        - Bisa di-extend (misalnya menambah captcha atau field custom).

    - Kekurangan:
        - Terbatas pada field default (username, password).
        - Jika aplikasi butuh autentikasi yang lebih kompleks (misalnya email + OTP), perlu kustomisasi.
        - UI default sangat sederhana, biasanya harus diubah agar sesuai dengan desain frontend.

    2. **Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?**
    Autentikasi (Authentication): proses memverifikasi identitas pengguna.
    Contoh: mengecek apakah username dan password cocok dengan data di database.

    Otorisasi (Authorization): proses menentukan hak akses pengguna setelah berhasil diautentikasi.
    Contoh: admin boleh mengakses dashboard admin, user biasa tidak boleh.

    Implementasi di Django:
    - Autentikasi:
        - django.contrib.auth menyediakan sistem login/logout.
        - Middleware AuthenticationMiddleware menghubungkan user dengan request (request.user).
        - AuthenticationForm atau mekanisme custom (misalnya authenticate() function).

    - Otorisasi:
        - Django menyediakan sistem permissions (has_perm, has_module_perms).
        - Sistem groups untuk memberi hak akses ke banyak user sekaligus.
        - Decorator seperti @login_required, @permission_required, dan @user_passes_test.

    3. **Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?**
    Session
    - Kelebihan:
        - Data disimpan di server, lebih aman (client hanya simpan session ID).
        - Bisa menyimpan data dalam jumlah besar.
        - Lebih fleksibel (misalnya menyimpan objek user, cart, dsb).

    - Kekurangan:
        - Membutuhkan storage di server (database, cache, file).
        - Membebani server jika ada banyak user.
        - Perlu mekanisme cleanup session yang expired.

    Cookies
    - Kelebihan:
        - Disimpan di browser client, tidak membebani server.
        - Mudah digunakan untuk menyimpan preferensi user (tema, bahasa).
        - Tidak butuh penyimpanan server tambahan.

    - Kekurangan:
        - Ukuran terbatas (maksimal ~4KB per cookie).
        - Rentan terhadap manipulasi (user bisa edit cookie).
        - Berpotensi menjadi target serangan XSS atau session hijacking.

    4. **Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**
    Tidak sepenuhnya aman. Ada risiko jika tidak dikonfigurasi dengan benar, antara lain:
    - Session hijacking → jika cookie sessionid dicuri, penyerang bisa login sebagai user sah.
    - XSS (Cross-Site Scripting) → cookie bisa dicuri lewat JavaScript jahat.
    - CSRF (Cross-Site Request Forgery) → attacker bisa menyalahgunakan cookie session untuk mengirim request palsu.

    Django menangani keamanan cookies dengan cara:
    - HttpOnly Cookie → cookie tidak bisa diakses lewat JavaScript (default di SESSION_COOKIE_HTTPONLY=True).
    - Secure Cookie → hanya dikirim lewat HTTPS (SESSION_COOKIE_SECURE=True).
    - CSRF Protection → Django otomatis menambahkan token CSRF untuk form POST.
    - Signed Cookies → jika menggunakan django.core.signing, Django menandatangani cookie agar tidak bisa dimanipulasi sembarangan.
    - Session Framework → menyimpan data sensitif di server, bukan langsung di cookie client.

6. **Melakukan add-commit-push ke GitHub.**
    git add .
    git commit -m "Tugas 4"
    git push origin master 
    git push pws master


**Tugas 5**
Pada tugas ini, kamu akan mengimplementasikan desain web berdasarkan beberapa hal yang sudah kamu pelajari selama tutorial (CSS, Framework, dsb).

Checklist untuk tugas ini adalah sebagai berikut:

1. **Implementasikan fungsi untuk menghapus dan mengedit product.**
    tambah fungsi edit_product dan delete_product di views.py dan tambahkan import dan path di urls.py

    buat berkas HTML baru : edit_product.html dan delete_product.html di subdirektori main/templates

    pada main/templates/main.html tambahkan edit dan delete

2. **Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:**
    1. Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.
        tambahkan tailwindcss di templates/base.html

        konfigurasi static files pada aplikasi 
        tambahkan pada settings.py
        pada bagian MIDDLEWARE (dibawah SecurityMiddleware): 'whitenoise.middleware.WhiteNoiseMiddleware',

        variabel STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL dikonfigurasikan
        if DEBUG:
            STATICFILES_DIRS = [
                BASE_DIR / 'static' # merujuk ke /static root project pada mode development
            ]
        else:
            STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production

        styling dengan Tailwind dan External CSS
        menambahkan static/css/global.css

        menghubungkan global.css dan script Tailwind ke base.html

        style login, register, add product, edit product, delete product

    2. Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
        1. Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
            pada main.html 
            <div class="w-32 h-32 mx-auto mb-4">
            <img src="{% static 'image/no-product.png' %}" alt="No product available" class="w-full h-full object-contain">
            </div>

        2. Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
            pada main.html
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {% for product in product_list %}
                    {% include 'card_product.html' with product=product %}
                {% endfor %}
            </div>

    3. Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
    pada main.html
        tambahkan button add and delete pada main/templates/card_product.html dan buat fungsi keduanya di views.py kemudian import serta tambahkan path di urls.py

    4. Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
        buat navbar.html di subdirektori templates
        
        tautkan navbar ke main/templates/main.html

        styling navbar
        buat style yang berbeda untuk device yang berbeda

3. **Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**
    1. Inline styles → style="color:red;" langsung di dalam elemen HTML. (paling kuat).
    2. ID selector → #header { color: blue; }
    3. Class, attribute, dan pseudo-class selector → .title {}, [type="text"] {}, :hover {}
    4. Element (tag) dan pseudo-element selector → p {}, h1 {}, ::before {} (paling lemah).
    5. Jika specificity sama → aturan yang ditulis terakhir (lebih bawah) di CSS yang dipakai.

4. **Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!**
    Responsive design = desain web yang menyesuaikan tampilan dengan berbagai ukuran layar (desktop, tablet, smartphone) agar pengalaman pengguna tetap nyaman.

    Mengapa penting?
    Saat ini mayoritas orang mengakses web lewat smartphone.
    Membuat UI konsisten di berbagai perangkat.
    Meningkatkan UX (User Experience) dan SEO (Google lebih suka website mobile-friendly).

    Contoh:
    Sudah menerapkan:
    - Tokopedia / Shopee → tampil rapi di HP maupun PC, navigasi tetap mudah.
    Belum menerapkan:
    - Website lama universitas / instansi → tampilan pecah, teks terlalu kecil di HP, pengguna harus zoom in/out.

5. **Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**
    Margin → memberi ruang di luar border.
    Border → garis yang mengelilingi elemen.
    Padding → memberi ruang di dalam border, antara konten dengan border.

    div {
        margin: 20px;      /* jarak antar elemen */
        border: 2px solid black; /* garis */
        padding: 10px;     /* jarak teks ke border */
    }

6. **Jelaskan konsep flex box dan grid layout beserta kegunaannya!**
    - Flexbox (Flexible Box Layout)
    Digunakan untuk menyusun elemen dalam 1 dimensi (baris atau kolom).
    Fleksibel: elemen bisa otomatis menyesuaikan ruang kosong.
    Berguna untuk: navbar, card yang sejajar, tombol yang rata.

    - Grid Layout
    Digunakan untuk menyusun elemen dalam 2 dimensi (baris & kolom).
    Lebih cocok untuk layout kompleks seperti dashboard, template majalah, dsb.
    Bisa mengatur area tertentu untuk elemen.

7. **Melakukan add-commit-push ke GitHub.**