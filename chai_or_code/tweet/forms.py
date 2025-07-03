from django import forms
from .models import Tweet

class TweetForm(forms.Model):
    class Meta:
        model = Tweet
        field = ['text','photo']
        