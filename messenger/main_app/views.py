from django.shortcuts import render
from django.views.generic import ListView

from chat.models import GroupChat


class GroupChatList(ListView):
    model = GroupChat
    template_name = 'chat/group_chat_list.html'
    context_object_name = 'group_chat_list'
