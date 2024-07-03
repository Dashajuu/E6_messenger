import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from profiles.models import Profile
from .services import create_or_add_group, create_group_message, create_private_message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope["user"]

        create_or_add_group(self.user, self.room_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.user.email
        profile = Profile.objects.get(user=self.user)

        create_group_message(self.user, message, self.room_name)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message, "user": user, "profile": profile}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        user = event["user"]
        profile = event["profile"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, "user": user, "profile": profile}))


class PrivateChatConsumer(WebsocketConsumer):
    def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.private_chat_name = f"chat_{self.chat_id}"
        self.user = self.scope["user"]

        async_to_sync(self.channel_layer.group_add)(
            self.private_chat_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.private_chat_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.user.email

        create_private_message(self.user, message, self.chat_id)

        # Send message to chat
        async_to_sync(self.channel_layer.group_send)(
            self.private_chat_name, {"type": "chat.message", "message": message, "user": user}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        user = event["user"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, "user": user}))
