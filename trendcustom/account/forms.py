from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator

from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "autocomplete": "text",
                "placeholder": "Enter login",
            }
        ),
        required=False,
        validators=[RegexValidator(r'[^0-9а-яА-ЯёЁ]', "Enter english login")],
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'placeholder': 'Enter email ',
            }
        ),
        required=False
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password ',
            }
        ),
        required=False
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repeat password ',
            }
        ),
        required=False
    )

    def clean_password1(self):
        password = self.cleaned_data['password1']
        if password == '':
            raise forms.ValidationError("Enter password", code="invalid")
        return password
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError("Enter login", code="invalid")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError("Enter email", code="invalid")
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(("Email address already in use."), code="duplicate")
        return email

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "password1", "password2")

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'text',
                'placeholder': 'Login',
            }
        ),
        required=False
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "autocomplete": "current-password",
                'placeholder': 'Password',
            }
        ),
        required=False
    )

    error_messages = {
        "invalid_login": (
            "Enter correct login and password"
        ),
    }

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == '':
            raise forms.ValidationError('Enter password', code='invalid')
        return password
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Enter login', code='invalid')
        if not User.objects.filter(username=username):
            raise forms.ValidationError('User not found', code='invalid')
        return username