from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic.edit import CreateView
from .forms import *


def index(request, category_id=None):
    cur_cat = Category.objects.get(pk=category_id) if category_id is not None else None
    if category_id is not None:
        context = {'Mes': Mes.objects.filter(category=cur_cat)}
    else:
        context = {'Mes': Mes.objects.all()}
    context['cur_cat'] = cur_cat
    return render(request, 'stena/index.html', context)


def message(request, mes_id):
    mes = get_object_or_404(Mes, pk=mes_id)
    return render(request, 'stena/message.html', {'mes': mes, })


class MesCreateView(CreateView):
    template_name = 'stena/create.html'
    form_class = MesForm
    success_url = reverse_lazy('index')


# def MesCreateView(request):
#     if request.method == 'POST':
#         form = MesForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 Mes.objects.create(**form.cleaned_data)
#             except:
#                 form.add_error(None, 'Ошибка добавления новости')
#             return redirect('index')
#     else:
#         form = MesForm()
#     return render(request, 'stena/create.html', {'form': form, })
