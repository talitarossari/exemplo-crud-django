from django.urls import path

from . import views

app_name = 'cliente'
urlpatterns = [
    path('lista/', views.ClienteListView.as_view(), name='lista'),
    path('<int:pk>/editar', views.ClienteUpdateView.as_view(), name='editar'),
]
