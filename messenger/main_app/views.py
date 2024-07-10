from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from chat.models import GroupChat


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
