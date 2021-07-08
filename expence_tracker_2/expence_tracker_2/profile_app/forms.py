from django import forms

from expence_tracker_2.profile_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


# class DeleteProfileForm(ProfileForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)