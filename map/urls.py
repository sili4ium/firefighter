from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main),
    path('<str:obj>', views.get_obj, name='map_obj'),
    path('<str:obj>/<str:area>', views.get_area, name='map_area'),
]