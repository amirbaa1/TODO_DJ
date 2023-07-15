from django.urls import path
from .views import ListTask, DetailTask, EditTask, CreateTask,DeleteTask

urlpatterns = [
    path('', ListTask.as_view(), name='home'),
    path("task/create/", CreateTask.as_view(), name="create"),
    path('task/<str:title>/', DetailTask.as_view(), name='detail'),
    path('task/<str:title>/update/', EditTask.as_view(), name='update'),
    path('task/<str:title>/Delete/', DeleteTask.as_view(), name='Delete'),
]
