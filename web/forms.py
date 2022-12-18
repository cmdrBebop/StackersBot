from django import forms

from .models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'external_id',
            'name',
        )
        widgets = {
            'name': forms.TextInput,
        }