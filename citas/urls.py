from django.urls import path
from . import views

app_name = "citas"

urlpatterns = [
    path("", views.lista_citas, name="lista"),
    path("nueva/", views.crear_cita, name="crear"),
    path("<int:pk>/editar/", views.editar_cita, name="editar"),
    path("<int:pk>/eliminar/", views.eliminar_cita, name="eliminar"),
]
