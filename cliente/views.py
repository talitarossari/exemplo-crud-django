from django.shortcuts import render
from django.urls import reverse_lazy
from cliente.models import Cliente
from django.views.generic.edit import UpdateView
from django.views import generic


# Classe responsavel por listar os clientes.
# Esta classe é generica, caso vocês queiram fazer algo especifico,
# é só jogar no google ou me perguntar. Evitem gambiarra
# Provavelmente tem um jeito bonito de se fazer.
class ClienteListView(generic.ListView):
    model = Cliente
    template_name = 'cliente_lista.html'
    context_object_name = 'clientes'


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente_editar.html'
    fields = '__all__'
    context_object_name = 'cliente'
    success_url = reverse_lazy('cliente:lista')
