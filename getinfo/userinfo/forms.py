from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, EducationalInfo


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, help_text='Enter a valid email address.')
    dob = forms.DateField(required=True, help_text='Enter your date of birth.')
    city = forms.CharField(max_length=100, required=True, help_text='Enter your city.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'dob', 'city')


class EducationalInfoForm(forms.ModelForm):
    class Meta:
        model = EducationalInfo
        fields = ['degree', 'university', 'graduation_year', 'subject', 'mobile_number']
