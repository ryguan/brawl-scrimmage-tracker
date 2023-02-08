from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='brawl-tag', max_length=100)