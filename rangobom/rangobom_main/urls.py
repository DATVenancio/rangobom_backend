from django.urls import path
from .views import companies,home

urlpatterns = [
    path("",home, name="home"),
    path("companies",companies,name="companies")
]