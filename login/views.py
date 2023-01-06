from django.shortcuts import render
from django.http import HttpResponse
def main(request):
    response = render(request, 'login/index.html')
    return HttpResponse(response)
