from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic.edit import CreateView
from .forms import *


def index(request, category_id=None):
    cats = Category.objects.all()
    cur_cat = Category.objects.get(pk=category_id) if category_id is not None else None
    if category_id is not None:
        context = {'Mes': Mes.objects.filter(category=cur_cat)}
    else:
        context = {'Mes': Mes.objects.all()}
    context['cats'] = cats
    context['cur_cat'] = cur_cat
    return render(request, 'stena/index.html', context)


def message(request, mes_id):
    mes = get_object_or_404(Mes, pk=mes_id)
    return render(request, 'stena/message.html', {'mes': mes, })


class MesCreateView(CreateView):
    template_name = 'stena/create.html'
    form_class = MesForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context

