from django.urls import path

from .import views

urlpatterns=[
    path("",views.count),
    path("destroy_session",views.delete_session),
    path("add_2",views.add_2),
]