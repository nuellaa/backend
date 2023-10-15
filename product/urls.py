from django.urls import path
from .views import hello,Create_food


urlpatterns = [
    path("fetchallfood/", hello),
    path("createfood/", Create_food)
]