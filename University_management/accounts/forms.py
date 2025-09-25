
from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    Full_name = forms.CharField(max_length=100, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('email', 'Full_name', 'password1', 'password2')

