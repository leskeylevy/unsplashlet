from django.shortcuts import render
from .models import Image

# Create your views here.


def image(request):
    images = Image.objects.all()
    for x in images:
        print(x.image_name)
    return render(request, 'image.html',{"images":images})
