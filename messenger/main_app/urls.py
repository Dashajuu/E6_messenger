from django.urls import path

from . import views


urlpatterns = [
    path("chats/", views.GroupChatList.as_view(), name="group_chat_list"),
]
