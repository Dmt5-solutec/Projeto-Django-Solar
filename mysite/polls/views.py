from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse("Hello, baby. You're at the polls index.")
    return render(request, 'home.html')
    

