from random import choice, random, randint
from .forms import GameCoinForm
from django.shortcuts import render


# Create your views here.


def coin(request, count):
    lst = []
    for _ in range(count):
        side = choice(['Орел', 'Решка'])
        lst.append(side)
    context = {'coin': 'монетка', 'value': lst}
    return render(request, 'gameapp/game_coin.html', context=context)


def cube(request, count):
    lst = []
    for _ in range(count):
        side = choice([1, 2, 3, 4, 5, 6])
        lst.append(side)
    context = {'cube': 'кубик', 'value': lst}
    return render(request, 'gameapp/game_cube.html', context=context)


def number(request, count):
    lst = []
    for _ in range(count):
        numbers = randint(0, 100)
        lst.append(numbers)
    context = {'number': 'случайное числло', 'value': lst}
    return render(request, 'gameapp/game_number.html', context=context)


def game_choice(requests):
    if requests.method == 'POST':
        form = GameCoinForm(requests.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if game == 'coin':
                return coin(requests, count)
            elif game == 'dice':
                return cube(requests, count)
            elif game == 'number':
                return number(requests, count)

    else:
        form = GameCoinForm()
        return render(requests, 'gameapp/game_c.html', {'form': form})
