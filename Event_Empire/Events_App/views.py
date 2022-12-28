from django.shortcuts import render
from .models import Event_Info

# Create your views here.

def home(request):
    events = Event_Info.objects.all()
    return render(request,"home.html", {'data':events})


def list(request):
    return render(request,"list.html")