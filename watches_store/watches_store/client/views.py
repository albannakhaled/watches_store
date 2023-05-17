from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request ,'pages/main.html')
def cart(request):
    return render(request,'pages/cart.html')