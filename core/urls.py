from django.urls import path
from django.conf.urls import url
from .views import home, celulares
from django.contrib.auth.views import LoginView,LogoutView
from core import views

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home2'),
    path('celulares/', celulares, name= 'celulares'),
    path('ingresar/', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('salir/', LogoutView.as_view(template_name='core/login.html'), name="logout"),
    path('registro/', views.signup, name='signup')
    
]
