from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        form = User
        field = ('name', 'email', 'created')