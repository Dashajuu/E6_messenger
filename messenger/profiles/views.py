from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
from .forms import MyProfileForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'
    raise_exception = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['current_user'] = self.request.user
        return context


@login_required(login_url="/accounts/login/")
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = MyProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(profile.get_absolute_url())
    else:
        form = MyProfileForm(instance=profile)

    return render(request, 'profiles/my_profile_update.html', {'form': form})
