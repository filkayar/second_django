from django.forms import ModelForm
from .models import *
import django.forms as forms
from stena.models import *

class MesForm(ModelForm):
    class Meta:
        model = Mes
        fields = ('title', 'content', 'price', 'category', 'photo')


# class MesForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Заголовок')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст сообщения')
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория новостей')
#     photo = forms.ImageField(label='Фотография')
#     price = forms.IntegerField(label='Цена (при её наличии)')
