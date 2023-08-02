from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .forms import NewPageForm

from bank_app.models import District


def home(request):
    districts = District.objects.all()
    return render(request, 'home.html', {'districts': districts})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def new_page(request):
    districts = District.objects.all()

    if request.method == 'POST':
        form = NewPageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application accepted.')
            return redirect('bank_app:new_page')
        else:
            return redirect('bank_app:new_page')
    return render(request, 'new_page.html', {'districts': districts})

def logout(request):
    auth.logout(request)
    return redirect('/')
def get(request):
    return render(request,'get_form.html')
