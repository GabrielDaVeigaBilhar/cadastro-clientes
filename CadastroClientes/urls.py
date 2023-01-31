from django.urls import re_path
from CadastroClientes import views

urlpatterns = [
    re_path(r'cliente$', views.clienteApi),
    re_path(r'cliente/([0-9]+)$', views.clienteConsultaId),
    re_path(r'cliente/([a-z]+)$', views.clienteConsultaNome),
    re_path(r'cliente/([0-9]+)$', views.clienteConsultaCPF),
]