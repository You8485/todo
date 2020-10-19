from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm


class userform(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),required=True,max_length=50)
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email ID'}),required=True,max_length=50)
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),required=True,max_length=50)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last Name'}),required=True,max_length=50)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),required=True,max_length=50)
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),required=True,max_length=50)

    class Meta():
        model = User
        fields = ['username','email','first_name','last_name','password','confirm_password']

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title','done']
