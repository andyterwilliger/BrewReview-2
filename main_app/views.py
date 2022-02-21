

from django.shortcuts import redirect, render

from django.http import HttpResponse

from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

from .models import Beer

from django.views.generic.edit import CreateView

def landing(request):
    return render(request, 'landing.html')

def feed(request):
    beers = Beer.objects.filter(user=request.user)
    return render(request, 'feed.html', {'beers':beers})
    

def about(request):
    return HttpResponse('<h1> About </h1>')

class BeerCreate(CreateView):
    model = Beer
    fields = '__all__'

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
