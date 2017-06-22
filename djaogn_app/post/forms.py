from django import forms
from .models import Post


class PostForm(forms.Form):  # forms의 ModelForm 클래스를 상속 받는다.
    comment = forms.CharField(widget=forms.Textarea)
