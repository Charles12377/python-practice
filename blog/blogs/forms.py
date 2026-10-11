from django import forms

from .models import Blog,Blog_post

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['text']
        labels={'text':''}

class Blog_postForm(forms.ModelForm):
    class Meta:
        model=Blog_post
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}
        