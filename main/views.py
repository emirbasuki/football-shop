from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'run station',
        'name': 'Emir Fadhil Basuki',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)