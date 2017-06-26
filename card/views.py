from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .models import Card

# Create your views here.
class Home(TemplateView):
    template_name = "card.html"

class CardCreateView(CreateView):
    model = Card
    fields = ['name', 'content']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CardCreateView, self).form_valid(form)


