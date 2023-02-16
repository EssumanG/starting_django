from django.urls import path
from . import views

urlpatterns = [
    path("home_page/", views.home, name="home_page"),
    path("tasks_list/", views.list_tasks, name="tasks_list"),
    path("task/<int:task_id>/", views.task_detail, name="task_detail"),
    path("task/update/<int:task_id>/", views.update_task, name="update_task"),
    path("task/delete/<int:task_id>/", views.delete_task, name="delete_task")
]
