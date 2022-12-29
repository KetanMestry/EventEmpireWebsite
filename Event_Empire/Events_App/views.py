from django.shortcuts import render
from django.template import loader
from .models import Event_Info
from .forms import EventForm

# Create your views here.




def home(request):
    print(request.method)
    events = Event_Info.objects.values("City").distinct()
    
    return render(request,"home.html",{'data': events})



# def EventForm(request):
#     print(request.method)
#     if request.method=="POST":
#         ef = EventForm(request.POST)
       
#         if ef.is_valid():
           
#             pt = ef.cleand_data["Party_Type"]
#             st = ef.cleand_data['State']
#             ct = ef.cleand_data["City"]
    
#     print("************************************************", ct)
            
            
    
            
            
    # else :
    #     ef = EventForm()
    # return render(request,"home.html",{'form': ef, 'data': 'hello','inData':st})
        
        
# def cityForm(request):
#     ef = EventForm()
#     return render(request,'home.html',{'form':ef})
        

        
        
    
def list(request):
    # print(request.method)
    if request.method=="POST":
        ef = EventForm(request.POST)
        print("************************************************",ef.data)
        # global ct
        
       
        
       
        
        ct = ef.data["city"]
        pt=ef.data["partyTypeSelector"]
        if( int(pt) == 1):
            partyType = "24-12-2022"
        else:
            partyType = "31-12-2022"
            
        print(pt)
        print(partyType)

        # if ef.is_valid():
            # pt = ef.cleand_data["Party_Type"]
            
            # print("************************************", ct)

            
        event = Event_Info.objects.filter(City=ct,Date=partyType)
        return render(request,"list.html" ,{'data': event})
    


def book(request):
    ticket = Event_Info.objects.all()
    return render (request,"book.html",{'data':ticket })

