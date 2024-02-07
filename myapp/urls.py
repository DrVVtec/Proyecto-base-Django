from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index,name="myapp_index"),
    path("proyects/",views.proyects,name="myapp_proyects"),
    path("create_proyect/",views.create_proyect,name="myapp_create_proyect"),
    path("tasks/",views.tasks,name="myapp_tasks"),
    path("proyect_tasks/<int:id>",views.proyect_tasks,name="myapp_proyect_tasks"),
    path("create_task/<int:id>",views.create_task,name="myapp_create_task"),
    path("delete_task/<int:id_t>",views.delete_task,name="myapp_delete_task"),
    path("about/", views.about,name="myapp_about")
]
