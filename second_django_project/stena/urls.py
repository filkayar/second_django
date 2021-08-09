from .views import *
from django.urls import path


urlpatterns = [
    path('<int:category_id>/', index, name='cat'),
    path('', index, name='index'),
    path('add/', MesCreateView.as_view(), name='add'),
]