from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import AuthorForms, ImageForm
from .models import Author


# Create your views here.


def post_author(requests):
    if requests.method == 'POST':
        form = AuthorForms(requests.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            biog = form.cleaned_data['biog']
            birthday = form.cleaned_data['birthday']
            author = Author(firstname=firstname, lastname=lastname, email=email, biog=biog, birthday=birthday)
            author.save()
            return render(requests, 'formshop/index.html', {'answer': 'Автор добавлен!'})
    else:
        form = AuthorForms()

    return render(requests, 'formshop/index.html', {'form': form})


def fit(request):
    return render(request, 'formshop/fit.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'formshop/upload_image.html', {'form': form})
