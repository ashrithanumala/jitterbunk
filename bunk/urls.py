from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:userid>/", views.personal, name="personal"),
    path("addbunk", views.addbunk, name="addbunk")
]