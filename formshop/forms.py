from django import forms
from .models import Author


class AuthorForms(forms.ModelForm):
    """
    Если форма и модели соответсвуют то мы просто наследуем как показано на примере ниже
    """

    class Meta:
        model = Author
        fields = ['firstname', 'lastname', 'email', 'biog', 'birthday']


class ImageForm(forms.Form):
    image = forms.ImageField()