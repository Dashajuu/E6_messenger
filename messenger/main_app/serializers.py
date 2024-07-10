from rest_framework import serializers

from chat.models import GroupChat
from profiles.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'email']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'}
        }


class GroupChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupChat
        fields = [
            'id',
            'admin',
            'name',
        ]
