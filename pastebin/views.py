# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from pastebin.models import Paste


class PasteCreate(CreateView):
    model = Paste


class PasteDetail(DetailView):
    model = Paste
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(PasteDetail, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PasteList(ListView):
    model = Paste