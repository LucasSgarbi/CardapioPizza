from django.urls import path
from .views import IndexView, BebidaView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', BebidaView.as_view(), name='bebida'),
    path('', SobreView.as_view(), name='sobre'),

]