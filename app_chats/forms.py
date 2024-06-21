from django import forms
from .models import Messages


class SendMessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message', 'image']
