from django.forms import ModelForm
from .models import *


class MesForm(ModelForm):
    class Meta:
        model = Mes
        fields = ('title', 'content', 'price', 'category', 'photo')
