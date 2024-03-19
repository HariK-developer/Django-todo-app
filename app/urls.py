from django.urls import path
from .views import index,create_todo,delete_todo,mark_todo



urlpatterns = [
    path("", index, name="")
]

htmxpatterns = [
    path('create_todo/', create_todo, name='create_todo'),
    path('delete_todo/<int:pk>/', delete_todo, name='delete_todo'),
    path('mark_todo/<int:pk>/', mark_todo, name='mark_todo'),
]

urlpatterns += htmxpatterns

