from django.urls import path
from . import views

urlpatterns = [
    path('',          views.inicio,     name='blog-home'),
    path('acerca/',   views.acerca,     name='blog-acerca'),
    path('contacto/', views.contacto,   name='blog-contacto'),
    path('registro/', views.registro,   name='blog-registro'),
    path('login/',    views.login_vista, name='blog-login'),
    path('post/<slug:slug>/',      views.detalle_post, name='blog-detalle'),
]