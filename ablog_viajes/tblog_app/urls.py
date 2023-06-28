from django.urls import path
from .views import HomeView, ArticuloDetailView, AgregarArticuloView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('articulo/<int:pk>', ArticuloDetailView.as_view(), name='articulo-detalle'), #cada publicacion tiene un id (primarykey) el primer post sera --> publicacion/1 y asi... 
    path('agregar_articulo/', AgregarArticuloView.as_view(), name='agregar_articulo'),
]