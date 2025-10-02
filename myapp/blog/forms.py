from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterForm(forms.ModelForm):
    username =forms.CharField(label="username",max_length=100,required=True)
    email = forms.CharField(label="email",max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data
class login_form(forms.Form):
    username = forms.CharField(label="username",max_length=100,required=True)
    password = forms.CharField(label="password",max_length=100,required=True)
    
    def clean(self):
        clean_data = super().clean()
        username = clean_data.get('username')
        password = clean_data.get('password')
          
        if username and password:
            user = authenticate(username= username, password=password)
            if user is None:
                raise forms.ValidationError("User not found!")
             
