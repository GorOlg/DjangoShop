from django import forms


class GameCoinForm(forms.Form):
    game = forms.ChoiceField(choices=(('coin', 'Монетка'), ('dice', 'Кости'), ('number', 'Случайное число')))
    count = forms.IntegerField(min_value=1, max_value=50)
