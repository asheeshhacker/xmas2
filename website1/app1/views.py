from django.shortcuts import render ,redirect
from .models import form1
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def sendletter(request):
     
    name1 = str(request.POST.get('name'))
    print(name1)
    wish1 = str(request.POST.get('wish'))
    address1 = str(request.POST.get('Address'))
    number1 = str(request.POST.get('Number'))
    messages.success(request, "Your letter has been submitted successfully!")

    form1(name = name1,wish = wish1,address = address1,number = number1).save()
    
    return redirect(index)