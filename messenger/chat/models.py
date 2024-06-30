from django.db import models

from profiles.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sender')
    content = models.TextField()
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class GroupMessage(Message):
    group = models.ForeignKey('GroupChat', on_delete=models.CASCADE)


class GroupChat(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_user')
    name = models.CharField(max_length=150)
    members = models.ManyToManyField(User, through='Membership', related_name='member_user')

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)


class PrivateMessage(Message):
    private_chat = models.ForeignKey('PrivateChat', on_delete=models.CASCADE)


class PrivateChat(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='private_chat_user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='private_chat_user2')

    class Meta:
        unique_together = ['user1', 'user2']
