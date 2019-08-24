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
from funilaria import views as funilaria_views
from usuario import views as usuario_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/',cliente,name='cliente'),
   
    path('',funilaria_views.index),
    re_path(r'cliente/(?P<id>\d+)/$',funilaria_views.editar_cliente, name='editar_cliente'),
    re_path(r'cliente/deletar/(?P<id>\d+)/$',funilaria_views.deletar_cliente, name='deletar_cliente'),
    path('formcliente/', funilaria_views.novocliente, name='formcliente'),

    
    re_path(r'cliente/(?P<id>\d+)/$',funilaria_views.editar_cliente, name='editar_cliente'),
    re_path(r'cliente/deletar/(?P<id>\d+)/$',funilaria_views.deletar_cliente, name='deletar_cliente'),
    path('formcliente/', funilaria_views.novocliente, name='formcliente'),
    
    
    path('empresa/',funilaria_views.empresa,name='empresa'),

    re_path(r'empresa/(?P<id>\d+)/$',funilaria_views.editar_empresa, name='editar_empresa'),
    re_path(r'empresa/deletar/(?P<id>\d+)/$',funilaria_views.deletar_empresa, name='deletar_empresa'),
    path('formempresa/', funilaria_views.novoempresa, name='formempresa'),

    path('perfil/',usuario_views.perfil_usuario,name='perfil_usuario'),
    path('novo-usuario/',usuario_views.novo_usuario,name='novo_usuario'),
    path('perfil/editar/',usuario_views.editar_usuario,name='formusuario'),
    path('perfil/senha/',usuario_views.alterar_senha,name='alterarsenha'),

    path('login/', usuario_views.login_user),
    path('login/submit', usuario_views.submit_login),
    path('logout/', usuario_views.logout_user),
]