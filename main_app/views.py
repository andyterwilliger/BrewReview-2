

from django.shortcuts import redirect, render

from django.http import HttpResponse

from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Beer, Photo

import uuid

import boto3

S3_BASE_URL= 'https://s3.us-east-1.amazonaws.com/'
BUCKET='brewreview'

from django.views.generic.edit import CreateView, UpdateView, DeleteView

def landing(request):
    return render(request, 'landing.html')

@login_required
def feed(request):
    beers = Beer.objects.filter(user=request.user)
    return render(request, 'feed.html', {'beers':beers})

@login_required
def beers_detail(request, beer_id):
    beer=Beer.objects.get(id=beer_id)
    return render(request, 'detail.html', {'beer' : beer})

def about(request):
    return render(request, 'about.html')


class BeerCreate(LoginRequiredMixin, CreateView):
    model = Beer
    fields = ('__all__')


class BeerDelete(LoginRequiredMixin, DeleteView):
    model = Beer
    success_url = '/beers/'

class BeerUpdate(LoginRequiredMixin, UpdateView):
    model = Beer
    fields = ['brewery', 'name', 'profile']

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
        else:
            error_message = 'Invalid credentials! Please try again.'
        
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def add_photo(request, beer_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, beer_id=beer_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', beer_id=beer_id)