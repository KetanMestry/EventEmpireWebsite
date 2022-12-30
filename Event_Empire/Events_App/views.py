from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Event_Info
from .forms import EventForm

from .models import User_Info

# Create your views here.




def home(request):
    print(request.method)
    cityList = Event_Info.objects.values("City").distinct()
    
    # stateList = Event_Info.objects.values("State").distinct()

    # print("*********************" , stateList)
    
    # return render(request,"home.html",{'data': stateList})
    return render(request,"home.html",{'data': cityList})



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
    if request.method=="POST":
        ef = EventForm(request.POST)
       
        ct = ef.data["city"]
        pt=ef.data["partyTypeSelector"]
   
        if( int(pt) == 1):
            partyType = 1
           
        else:
            partyType = 2
            
       

        if ef.is_valid():
            pt = ef.cleand_data["Party_Type"]
     
            
        event = Event_Info.objects.values().filter(City__icontains=ct,Party_Type= partyType)
        
        return render(request,"list.html" ,{'data': event, 'pType':partyType, 'selCity':ct } )
    elif request.method =="GET":
        ef = EventForm(request.GET)
      
        selectedPartyType = ef.data['pVal']
        selectedCity = ef.data['cVal']
             
        event = Event_Info.objects.values().filter( City__icontains=selectedCity,Party_Type= selectedPartyType)
        
        return render(request,"list.html" ,{'data': event,'pType':selectedPartyType, 'selCity':selectedCity } )


        
        
        
def book(request):
    if request.method=="POST" :
        ef = EventForm(request.POST)
        
        Full_Name=request.POST['fname']
        Email=request.POST['email']
        Address=request.POST['add']
        City=request.POST['city']
        State=request.POST['state']
        Pincode=request.POST['pin']
        Members=request.POST['mem']
        Contact=request.POST['con']
        Party_Id = ef.data['partyId']
        
        p=User_Info.objects.create(Full_Name=Full_Name,Email=Email,Address=Address,City=City,State=State,Pincode=Pincode,No_Of_Mems=Members,Contact_No=Contact, Party_Id = Party_Id )
        p.save()
        print(p)
        return redirect('/')
    elif request.method == "GET":
        ef = EventForm(request.GET)
      
        # print("**********************", ef.data)
        

        id = ef.data['eventId']
        
        pId = int(id)
        print(type(pId))
      
        event = Event_Info.objects.filter(id=pId)
        
        
       
        return render(request,"book.html",{'partyData':event} )
        # return HttpResponseRedirect("/book/")