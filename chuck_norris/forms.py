from django import forms

class JokeForm(forms.Form):
    first_name = forms.CharField(label="Voornaam")
    last_name = forms.CharField(label="Achternaam")