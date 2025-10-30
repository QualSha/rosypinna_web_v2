from django.urls import path
from . import views

urlpatterns = [
    # Path '' (root) akan memanggil fungsi views.home
    path('', views.home, name='home'),
]