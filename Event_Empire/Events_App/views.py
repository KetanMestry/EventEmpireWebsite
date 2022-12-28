from django.shortcuts import render
from django.template import loader
from .models import Event_Info

# Create your views here.

def home(request):
    events = Event_Info.objects.values("City").distinct()
    
    return render(request,"home.html",{'data': events})

    

        
        
    
def list(request):
    event = Event_Info.objects.filter(City= "MUMBAI", Party_Starting_Date="2022-12-24 8PM")
    return render(request,"list.html" ,{'data': event})