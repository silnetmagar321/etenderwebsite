from django.contrib.auth.models import User
from django import forms

from accounts.models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('company_name', 'contact_person_name', 'address', 'mobile_number')

