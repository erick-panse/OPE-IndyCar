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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [

    path('paginainicial/', funilaria_views.pagina_inicial),
    path('quemsomos/', funilaria_views.quemsomos),
    path('index/', funilaria_views.index),
    path('admin/', admin.site.urls),
    url(r'clientes/',cliente,name='cliente'),
   
    path('',funilaria_views.pagina_inicial),
    re_path(r'cliente/(?P<id>\d+)/$',funilaria_views.editar_cliente, name='editar_cliente'),
    re_path(r'cliente/deletar/(?P<id>\d+)/$',funilaria_views.deletar_cliente, name='deletar_cliente'),
    path('cliente/', funilaria_views.novocliente, name='cliente'),
    
    path('empresas/',funilaria_views.empresa,name='empresa'),
    re_path(r'empresa/(?P<id>\d+)/$',funilaria_views.editar_empresa, name='editar_empresa'),
    re_path(r'empresa/deletar/(?P<id>\d+)/$',funilaria_views.deletar_empresa, name='deletar_empresa'),
    path('empresa/', funilaria_views.novoempresa, name='empresa'),
    
    path('ordensdeservico/',funilaria_views.ordem_de_servico,name='ordensdeservico'),
    path('ordemdeservico/', funilaria_views.nova_os, name='ordemdeservico'),
    re_path(r'ordemdeservico/(?P<id>\d+)/$',funilaria_views.editar_os, name='editar_ordem'),
    re_path(r'ordemdeservico/deletar/(?P<id>\d+)/$',funilaria_views.deletar_os, name='deletar_ordem'),

    path('materiais/',funilaria_views.material,name='material'),
    path('material/', funilaria_views.novo_material, name='material'),
    re_path(r'material/(?P<id>\d+)/$',funilaria_views.editar_material, name='editar_material'),
    re_path(r'material/deletar/(?P<id>\d+)/$',funilaria_views.deletar_material, name='deletar_material'),

    path('perfil/',usuario_views.perfil_usuario,name='perfil_usuario'),
    path('novo-usuario/',usuario_views.novo_usuario,name='novo_usuario'),
    path('perfil/editar/',usuario_views.editar_usuario,name='formusuario'),
    path('perfil/editar/senha/',usuario_views.alterar_senha,name='alterarsenha'),

    path('login/', usuario_views.login_user),
    path('login/submit', usuario_views.submit_login),
    path('logout/', usuario_views.logout_user),
    re_path(r'add-no-carrinho/(?P<id>\d+)/$', add_no_carrinho, name='add_no_carrinho'),
    re_path(r'tirar-do-carrinho/(?P<id>\d+)/$', tirar_do_carrinho, name='tirar_do_carrinho'),
    re_path(r'remover-do-carrinho/(?P<id>\d+)/$', remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/', carrinho, name='order-summary'),

    path('orcamentos/',funilaria_views.orcamento,name='orcamentos'),
    re_path(r'orcamento/c/(?P<id>\d+)/$', funilaria_views.novo_orcamento, name='orcamento'),
    re_path(r'orcamento/(?P<id>\d+)/$',funilaria_views.editar_orcamento, name='editar_orcamento'),
    re_path(r'orcamento/deletar/(?P<id>\d+)/$',funilaria_views.deletar_orcamento, name='deletar_orcamento'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" path('orcamentos/',funilaria_views.orcamento,name='orcamento'),
    path('orcamento/', funilaria_views.novo_orcamento, name='orcamento'),
    re_path(r'orcamento/(?P<id>\d+)/$',funilaria_views.editar_orcamento, name='editar_orcamento'),
    re_path(r'orcamento/deletar/(?P<id>\d+)/$',funilaria_views.deletar_orcamento, name='deletar_orcamento'), """
