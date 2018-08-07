from django.urls import path

from . import views

app_name = 'cliente'
urlpatterns = [
    path('listar/', views.ClienteListView.as_view(), name='listar'),
    path('criar/', views.ClienteCreateView.as_view(), name='criar'),
    path('<int:pk>/editar', views.ClienteUpdateView.as_view(), name='editar'),
    path('<int:pk>/deletar', views.ClienteDeleteView.as_view(), name='deletar'),
]
