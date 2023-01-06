from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main),
    path('<int:ev_id>', views.get_ev),
]