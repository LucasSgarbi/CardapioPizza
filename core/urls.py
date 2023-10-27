from django.urls import path
from .views import IndexView, BebidaView, SobreView, RegisterView, PizzaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pizza', PizzaView.as_view(), name='pizza'),
    path('bebida', BebidaView.as_view(), name='bebida'),
    path('sobre', SobreView.as_view(), name='sobre'),
    path('cadastro', RegisterView.as_view(), name='cadastro'),

]