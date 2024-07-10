from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets

from .serializers import GroupChatSerializer, UserSerializer
from chat.models import GroupChat
from profiles.models import User, Profile


@login_required(login_url="/accounts/login/")
def home(request):
    return render(request, "chat/home.html")


class GroupChatList(LoginRequiredMixin, ListView):
    model = GroupChat
    ordering = '-pk'
    template_name = 'chat/group_chat_list.html'
    context_object_name = 'group_chat_list'
    raise_exception = False
    paginate_by = 10


class UserProfileList(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profile_list'
    raise_exception = False


class GroupChatViewset(viewsets.ModelViewSet):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
