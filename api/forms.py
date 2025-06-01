from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=True,
        error_messages={
            "required": "Please provide your name",
            "max_length": "Name too long (200 char max)",
        },
    )

    email = forms.EmailField(
        required=True,
        error_messages={
            "required": "Please provide your email",
            "invalid": "Please enter a valid email address",
        },
    )

    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
        max_length=10000,
        error_messages={
            "required": "Please provide a message",
            "max_length": "Message too long (10000 char max)",
        },
    )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) > 200:
            raise forms.ValidationError("Name too long (200 char max)")
        return name

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if len(message) > 10000:
            raise forms.ValidationError("Message too long (10000 char max)")
        return message
