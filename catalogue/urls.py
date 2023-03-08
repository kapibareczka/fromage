from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_cheese", views.add_cheese, name="add_cheese"),
    path("cheese/<int:id>", views.cheese_details, name="cheese_details"),
    path("review/<int:id>", views.review, name="review"),
    path("customer/<int:id>", views.customer, name="customer"),
    path("customer/<int:id>/add_review", views.add_review, name="add_review")
]