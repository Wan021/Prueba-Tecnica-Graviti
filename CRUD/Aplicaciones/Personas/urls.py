from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarPersona/', views.registrarPersona),
    path('edicionPersona/<codigo>', views.edicionPersona),
    path('editarPersona/', views.editarPersona),
    path('eliminacionPersona/<codigo>', views.eliminacionPersona),
    path('cancel/',views.cancelar),
    path('OrderNombre/',views.OrderNombre),
    path('OrderAPaterno/',views.OrderAPaterno),
    path('OrderAMaterno/',views.OrderAMaterno),
    path('OrderNacionalidad/',views.OrderNacionalidad),
    path('OrderEdad/',views.OrderEdad),
]