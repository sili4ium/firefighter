from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

stations = {
    'Obj-A': ['Area-1', 'Area-2'],
    'Obj-B': ['Area-3', 'Area-4'],
}

obj_positions = {
    'Obj-A': [300, 300],
    'Obj-B': [500, 500],
}

def main(request):
    response = render(request, 'map/cheme.html')
    return HttpResponse(response)

def get_obj(request, obj:str):
    stat = stations.get(obj)
    if stat:
        data = {
            'url': '/map',
            'pos': stat,
        }
        response = render(request, 'map/object.html', context=data)
        return HttpResponse(response)
    else:
        return HttpResponseNotFound(f"Error")

def get_area(request, obj:str, area:str):
    stat = stations.get(obj)
    if stat and area in stat:
        redirect_url = reverse('monitor', args=(obj, area))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"Error")
