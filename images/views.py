from django.shortcuts import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my hood')