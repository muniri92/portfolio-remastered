from django import forms


class ContactForm(forms.Form):
    """Forms class."""
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    message = forms.CharField(max_length=1000)
