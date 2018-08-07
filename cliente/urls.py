from django.urls import path

from . import views

app_name = 'cliente'
urlpatterns = [
    path('lista/', views.ClienteListView.as_view(), name='lista'),
]
