from django.shortcuts import render
from .models import Image

# Create your views here.


def image(request):
    images = Image.objects.all()
    # for x in images:
    #     print(x.image_name)
    return render(request, 'images.html',{"images":images})


def imagealone(request,image_id):
    try:
        image  = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"imageOne.html",{"image":image})
