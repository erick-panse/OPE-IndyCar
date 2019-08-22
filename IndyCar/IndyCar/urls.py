"""IndyCar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import re_path,path
from funilaria.views import *
from funilaria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/',cliente,name='cliente'),
   
    path('',views.submit_login),
    re_path(r'cliente/(?P<id>\d+)/$',editar_cliente, name='editar_cliente'),
    re_path(r'cliente/deletar/(?P<id>\d+)/$',deletar_cliente, name='deletar_cliente'),
    path('formcliente/', novocliente, name='formcliente'),

    
    re_path(r'cliente/(?P<id>\d+)/$',editar_cliente, name='editar_cliente'),
    re_path(r'cliente/deletar/(?P<id>\d+)/$',deletar_cliente, name='deletar_cliente'),
    path('formcliente/', novocliente, name='formcliente'),
    path('empresa/',cliente,name='empresa'),

    re_path(r'empresa/(?P<id>\d+)/$',editar_empresa, name='editar_empresa'),
    re_path(r'empresa/deletar/(?P<id>\d+)/$',deletar_empresa, name='deletar_empresa'),
    path('formempresa/', novoempresa, name='formempresa'),
    
    path('veiculo/',cliente,name='veiculo'),
   
    re_path(r'veiculo/(?P<id>\d+)/$',editar_veiculo, name='editar_veiculo'),
    re_path(r'veiculo/deletar/(?P<id>\d+)/$',deletar_veiculo, name='deletar_veiculo'),
    path('formveiculo/', novoveiculo, name='formveiculo'), 



    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user)
]