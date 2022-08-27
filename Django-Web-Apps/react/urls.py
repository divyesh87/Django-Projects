from django.urls import path
from  . import views

urlpatterns = [
    path("", views.index),
    path("<int:section>", views.loadsection),
    path("scroll", views.scroll)
] 