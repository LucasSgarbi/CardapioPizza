from django.urls import path, include
from .views import IndexView, BebidaView, SobreView, RegisterView, PizzaView, LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pizza', PizzaView.as_view(), name='pizza'),
    path('bebida', BebidaView.as_view(), name='bebida'),
    path('sobre', SobreView.as_view(), name='sobre'),
    path('cadastro', RegisterView.as_view(), name='cadastro'),
    path('login', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace="social")),

]