
from django.contrib.auth import get_user_model
from django import forms

from accounts.models import User

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    First_name = forms.CharField(max_length=100, required=True)
    Last_name = forms.CharField(max_length=100, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('email', 'First_name', 'Last_name', 'password1', 'password2')

    def password_checking(self):
            p1 = self.cleaned_data.get("password1")
            p2 = self.cleaned_data.get("password2")
            if p1 and p2 and p1 != p2:
                raise forms.ValidationError("Passwords does not match, Please try again")
            return p2