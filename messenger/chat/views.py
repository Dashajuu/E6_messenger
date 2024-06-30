from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import GroupChat, GroupMessage, Membership, PrivateChat, PrivateMessage
from profiles.models import User


@login_required(login_url="/accounts/login/")
def room(request, room_name):
    group = GroupChat.objects.filter(name=room_name).first()
    members = Membership.objects.filter(group=group)
    messages = GroupMessage.objects.filter(group=group).order_by('data_created')
    return render(request, "chat/room.html", {
        "room_name": room_name,
        'messages': messages,
        'members': members,
    })


@login_required(login_url="/accounts/login/")
def private_chat_view(request, pk):
    chat = PrivateChat.objects.get(pk=pk)
    messages = PrivateMessage.objects.filter(private_chat=chat).order_by('data_created')
    return render(request, 'chat/private_chat.html', {
        "chat_id": pk,
        'messages': messages,
    })


@login_required(login_url="/accounts/login/")
def create_private_chat(request):
    profile_user = request.GET.get('profile_user')

    current_user = request.user
    profile_user = User.objects.get(pk=profile_user)

    private_chat, created = PrivateChat.objects.get_or_create(user1=current_user, user2=profile_user)

    return redirect(reverse('private_chat', kwargs={'pk': private_chat.pk}))
