from django.urls import path

from . import views


urlpatterns = [
    path("<str:room_name>/", views.room, name="room"),
    path("private/<int:pk>/", views.private_chat_view, name='private_chat'),
    path('private/create_private_chat/', views.create_private_chat, name='create_private_chat'),
]
