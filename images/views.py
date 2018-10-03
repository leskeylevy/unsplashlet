from django.shortcuts import render
from .models import *

# Create your views here.


def image(request):
    images = Image.objects.all()
    location = Location.objects.all()
    return render(request, 'images.html',{"images":images,"location":location})

def locations(request,location_id):
    loc = Location.objects.get(location=location_id)
    location = Image.objects.filter(location=loc.id)
    locs = Location.objects.all()
    catego = Category.objects.all()
    return render(request,'location.html',{"location":location,"catego":catego,"locs":locs})

# def imagealone(request,image_id):
#     try:
#         image  = Image.objects.get(id=image_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"imageOne.html",{"image":image})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html', {"message": message})
