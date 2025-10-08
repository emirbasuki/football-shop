from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
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

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description' : product.description,
            'thumbnail' : product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'stock' : product.stock,
            'brand' : product.brand,
            'size' : product.size,
            'product_views': product.product_views,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description' : product.description,
            'thumbnail' : product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'stock' : product.stock,
            'brand' : product.brand,
            'size' : product.size,
            'product_views': product.product_views,
            'user_id': product.user_id,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
      form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# Create Ajax
@login_required
@require_POST
def add_product_entry_ajax(request):
    form = ProductForm(request.POST)
    if not form.is_valid():
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    product = form.save(commit=False)
    product.user = request.user
    product.save()
    return JsonResponse({'status': 'success', 'product': {
        'id': str(product.id),
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'thumbnail': product.thumbnail,
        'category': product.category,
        'is_featured': product.is_featured,
        'stock': product.stock,
        'brand': product.brand,
        'size': product.size,
        'product_views': product.product_views,
        'created_at': product.created_at.isoformat() if product.created_at else None,
        'user_id': product.user_id,
    }}, status=201)


@login_required
@require_POST
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user_id != request.user.id:
        return HttpResponseForbidden(JsonResponse({'status': 'error', 'message': 'Not allowed'}))
    form = ProductForm(request.POST, instance=product)
    if not form.is_valid():
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    product = form.save()
    return JsonResponse({'status': 'success', 'product': {'id': str(product.id), 'name': product.name, 'user_id': product.user_id}})


@login_required
@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user_id != request.user.id:
        return HttpResponseForbidden(JsonResponse({'status': 'error', 'message': 'Not allowed'}))
    product.delete()
    return JsonResponse({'status': 'success', 'message': 'Deleted'})


# AJAX login/register
@require_POST
def login_ajax(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        auth_login(request, user)
        return JsonResponse({'status': 'success', 'message': 'Login successful'})
    return JsonResponse({'status': 'error', 'errors': form.errors}, status=401)


@require_POST
def register_ajax(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        return JsonResponse({'status': 'success', 'message': 'Account created'})
    return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)