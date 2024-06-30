from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'
    raise_exception = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['current_user'] = self.request.user
        return context
