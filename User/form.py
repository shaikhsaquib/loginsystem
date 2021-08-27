
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class UserForm(UserCreationForm):
    class Meta:
        password2=forms.CharField(label='confirm Password (again)',
        widget=forms.PasswordInput)
        model=User
        fields=['email','username']


class editPostForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','email',]
        labels={'email':'Email'}