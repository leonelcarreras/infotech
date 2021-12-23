from django import forms
from .models import Comment, Post
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content', )



class CreateUserForm(UserCreationForm):
    email = forms.EmailField()    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class OrderForm(ModelForm):
    
    content = forms.CharField()

    class Meta:
        model = Post
        fields = ['title', 'overview', 'content', 'thumbnail', 'categories', 'featured']
