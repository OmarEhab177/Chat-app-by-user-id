from django.urls import path

from . import views


urlpatterns = [
    path("", views.select_user, name="select_user"),
    path("chat/", views.chat_page, name="chat_page"),
]