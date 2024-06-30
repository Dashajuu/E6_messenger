from django import forms

from .models import Profile


class MyProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'second_name',
            'username',
            'avatar',
        ]
