from django.shortcuts import render
from .models import List
#from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items':all_items })
def about(request):
    return render(request, 'about.html', {})
