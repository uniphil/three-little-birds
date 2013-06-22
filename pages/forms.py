from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True)
    cc = forms.BooleanField(required=False)
    message = forms.CharField()
