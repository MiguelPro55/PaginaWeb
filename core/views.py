from django.shortcuts import render, redirect
from .models import Marca, Celular, Carrito, Login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

# Create your views here.

@login_required
def home(request):
    return render(request, 'core/home.html')

    
@login_required
def celulares(request):
    Celulares_List = Celular.objects.all()
    return render(request, 'core/celulares.html',{
       'Celulares_List':Celulares_List
    } )

def login(request, user):
	return render(request, 'core/login.html')



def signup(request): 
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = UserCreationForm()
	return render(request, 'core/registro.html',{
		'form': form
	

	})









