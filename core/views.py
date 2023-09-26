from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class BebidaView(TemplateView):
    template_name = 'bebida.html'
    success_url = reverse_lazy('bebida')

    def get_context_data(self, **kwargs):
        context = super(BebidaView, self).get_context_data(**kwargs)
        return context


class SobreView(TemplateView):
    template_name = 'sobre.html'
    success_url = reverse_lazy('sobre')

    def get_context_data(self, **kwargs):
        context = super(SobreView, self).get_context_data(**kwargs)
        return context
