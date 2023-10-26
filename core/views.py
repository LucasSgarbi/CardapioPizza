from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForms


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


class SobreView(FormView):
    template_name = 'sobre.html'
    success_url = reverse_lazy('sobre')
    form_class = ContatoForms

    def get_context_data(self, **kwargs):
        context = super(SobreView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(SobreView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enivar o E-mail')
        return super(SobreView, self).form_invalid(form, *args, *kwargs)


class RegisterView(TemplateView):
    template_name = 'cadastro.html'
    success_url = reverse_lazy('cadastro')

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        return context
