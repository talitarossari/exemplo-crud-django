from django.shortcuts import render
from cliente.models import Cliente
from django.views import generic


# Classe responsavel por listar os clientes.
# Esta classe é generica, caso vocês queiram fazer algo especifico,
# é só jogar no google ou me perguntar. Evitem gambiarra
# Provavelmente tem um jeito bonito de se fazer.
class ClienteListView(generic.ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'
