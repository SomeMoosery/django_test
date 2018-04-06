from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: #Which model should be used to create the form
        model = Post #We want to use the Post model to create the form
        fields = ('title', 'text') #We only want title and text to be available to edit!
