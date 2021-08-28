from django.conf import settings
from django.conf.urls.static import static

from .views import *
from django.urls import path

urlpatterns = [
    path('<int:category_id>/', index, name='cat'),
    path('', index, name='index'),
    path('add/', MesCreateView.as_view(), name='add'),
    # path('add/', MesCreateView, name='add'),
    path('mes/<int:mes_id>', message, name='message'),
]

# Менеджер для подгрузки изображений при запросе к оным
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
