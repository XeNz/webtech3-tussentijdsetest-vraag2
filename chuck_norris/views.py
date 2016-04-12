from django.shortcuts import render
from django import forms
from .forms import JokeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
import random
from django.core.urlresolvers import reverse
from .models import Author,Joke
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def fill_db():
	r.set('author:1', "Winston Churchill")
	r.set('author:2', "Albert Einstein")
	r.set('author:3', "W. C. Fields")
	r.set('joke:1:1', "I may be drunk, Miss, but in the morning I will be sober and you will still be ugly.")
	r.set('joke:1:2', "You have enemies? Good. That means you've stood up for something, sometime in your life.")
	r.set('joke:3:1', "I never drink water because of the disgusting things that fish do in it.")
	r.set('joke:3:2', "No doubt exists that all women are crazy; it's only a question of degree.")
	r.set('joke:2:1', "Try not to become a man of success, but rather try to become a man of value.")
	r.set('joke:2:2', "The true sign of intelligence is not knowledge but imagination.")


def index(request):
  #   if request.method == 'POST':
  #       form = JokeForm(request.POST)
  #       firstname = request.POST.get('first_name', '')
  #       lastname = request.POST.get('last_name', '')

  #       authorobject = Author.objects.filter(Q(first_name__icontains=firstname) & Q(last_name__icontains=lastname))
  #       if authorobject is not None:
  #       	randomobject = random.choice(authorobject.select_related('joke'))
  #       	url = reverse('details', kwargs={'joke': randomobject})
		# return HttpResponseRedirect(url)
        

  #   else:
    form = JokeForm()

    return render(request, 'index.html', {'form': form})

def detail(request, first_name,last_name):
    if request.method == 'POST':
        form = JokeForm(request.POST)
        firstname = request.POST.get('first_name', '')
        lastname = request.POST.get('last_name', '')

        authorobject = Author.objects.filter(Q(first_name__icontains=firstname) & Q(last_name__icontains=lastname))
        if authorobject is not None:
        	randomobject = random.choice(authorobject.select_related('joke'))
        	url = reverse('details', kwargs={'joke': randomobject})
		return HttpResponseRedirect(url)
        

    else:
        form = JokeForm()

    return render(request, 'details.html')
    

