from django.urls import path
from .views import IndexView, BebidaView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('bebida', BebidaView.as_view(), name='bebida'),
    path('sobre', SobreView.as_view(), name='sobre'),

]