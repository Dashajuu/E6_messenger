from django.shortcuts import render
from django.views.generic import DetailView

from .models import Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['current_user'] = self.request.user
        return context
