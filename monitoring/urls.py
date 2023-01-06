from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.no_area_info),
    path('<str:obj>/<str:area>', views.get_area_info, name="monitor")
]
