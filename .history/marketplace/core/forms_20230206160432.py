from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username'
        'class': 'w-full py-4 px-6 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500'
    }))