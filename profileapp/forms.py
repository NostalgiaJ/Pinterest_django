from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        models = Profile
        fields = ['image', 'nickname', 'message']
