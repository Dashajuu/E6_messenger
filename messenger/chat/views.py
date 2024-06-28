from django.shortcuts import render

from .models import GroupChat, GroupMessage, Membership


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    group = GroupChat.objects.filter(name=room_name).first()
    members = Membership.objects.filter(group=group)
    messages = GroupMessage.objects.filter(group=group).order_by('data_created')
    return render(request, "chat/room.html", {
        "room_name": room_name,
        'messages': messages,
        'members': members,
    })


def private_chat(request, pk):
    return render(request, 'chat/private_chat.html', {"chat_id": pk})
