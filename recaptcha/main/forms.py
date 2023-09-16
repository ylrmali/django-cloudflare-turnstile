from turnstile.fields import TurnstileField
from django import forms

class Forms(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    turnstile = TurnstileField(theme='light', label='')



    def clean(self):
        cleaned_data = super().clean()
        turnstile = cleaned_data.get('turnstile')
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not turnstile:
            raise forms.ValidationError('Please complete the captcha')
        return cleaned_data
