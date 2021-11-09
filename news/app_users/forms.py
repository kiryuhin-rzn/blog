from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app_users.models import Account


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExtendedRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class BalanceForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('balance',)



#class ExtendedRegisterForm(UserCreationForm)