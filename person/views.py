from django.shortcuts import render
from django.http import HttpResponse
def main(request):
    data = {

    }
    response = render(request, 'person/main.html', context=data)
    return HttpResponse(response)
