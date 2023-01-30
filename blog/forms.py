from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Comment, Post, Customer


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (  'body', )
        widgets = {
            'body': forms.Textarea(attrs={'rows': 6, 'cols': 100, 'placeholder': 'Write your review:','class': 'input textarea'})
        }
        labels = {
            'body': ''
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'intro', 'body', 'image',)
        
        widgets = {
        'title': forms.TextInput(attrs={'size': '50', 'class': 'input is-success is-rounded', 'style':'margin:10px;'}),
        'intro': forms.TextInput(attrs={'placeholder': 'Write a good intro for you post.', 'size': '50', 'class': 'input is-success is-rounded', 'style':'margin:10px;'}),
        'body': forms.Textarea(attrs={'rows': 6, 'cols': 100, 'placeholder': 'Write all the content here:', 'class':'input textarea'}),
        'image': forms.ClearableFileInput(attrs={'multiple': True, 'class':'button is-rounded'})
    }



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user','profile_pic']

        widgets = {
        'name': forms.TextInput(attrs={'size': '50', 'class': 'input is-success is-rounded', 'style':'margin:10px;'}),
        'company': forms.TextInput(attrs={'size': '50', 'class': 'input is-success is-rounded', 'style':'margin:10px;'}),
        'role': forms.TextInput(attrs={'size': '50', 'class': 'input is-success is-rounded', 'style':'margin:10px;'}),
        'skills': forms.Textarea(attrs={'rows': 6, 'cols': 100, 'placeholder': 'Write your main skills today:', 'class': 'input textarea', 'style':'margin:10px;'}),
        'interests': forms.Textarea(attrs={'rows': 6, 'cols': 100, 'placeholder': 'Write the skill you want to learn:', 'class': 'input textarea', 'style':'margin:10px;'}),
    }

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('profile_pic',)

        widgets = {
        'profile_pic': forms.ClearableFileInput(attrs={'multiple': True, 'class':'button is-rounded', 'style':'margin:10px;'})
    }
        labels={
            'profile_pic':''
        }