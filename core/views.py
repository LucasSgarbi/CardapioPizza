from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForms
from .models import Produto, Combo


class IndexView(TemplateView):
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['titulo'] = 'Home'
        context['combo'] = Combo.objects.all()
        return context


class PizzaView(TemplateView):
    template_name = 'pizza.html'
    success_url = reverse_lazy('pizza')

    def get_context_data(self, **kwargs):
        context = super(PizzaView, self).get_context_data(**kwargs)
        context['pizzaSalgada'] = Produto.objects.all().filter(categoria_id=2)
        context['pizzaDoce'] = Produto.objects.all().filter(categoria_id=4)
        context['titulo'] = 'Pizza'
        return context


class BebidaView(TemplateView):
    template_name = 'bebida.html'
    success_url = reverse_lazy('bebida')

    def get_context_data(self, **kwargs):
        context = super(BebidaView, self).get_context_data(**kwargs)
        context['bebidaNA'] = Produto.objects.all().filter(categoria_id=3)
        context['bebidaA'] = Produto.objects.all().filter(categoria_id=1)
        context['titulo'] = 'Bebidas'
        return context


class SobreView(FormView):
    template_name = 'sobre.html'
    success_url = reverse_lazy('sobre')
    form_class = ContatoForms

    def get_context_data(self, **kwargs):
        context = super(SobreView, self).get_context_data(**kwargs)
        context['titulo'] = 'Sobre'
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
        context['titulo'] = 'Cadastro'
        return context


class LoginView(TemplateView):
    template_name = 'login.html'
