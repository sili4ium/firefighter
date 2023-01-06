from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main),
    path('<int:note_id>', views.get_note_info)
]