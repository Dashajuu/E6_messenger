from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("group_chat_list/", views.GroupChatList.as_view(), name="group_chat_list"),
    path("profiles/", views.UserProfileList.as_view(), name="profile_list"),
]
