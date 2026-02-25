from django.urls import path
from .views import index
from .views import contatos


urlpatterns = [
    path('', index, name="urlindex"),
    path('contatos', contatos, name="urlcontatos"),
]
