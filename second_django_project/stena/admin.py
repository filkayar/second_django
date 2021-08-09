from django.contrib import admin
from .models import *
# Register your models here.


class MesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('title', 'id', 'published')


admin.site.register(Mes, MesAdmin)
admin.site.register(Category)
