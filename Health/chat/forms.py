from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control message-input',
                'placeholder': 'Type your message here...',
                'autocomplete': 'off'
            })
        }