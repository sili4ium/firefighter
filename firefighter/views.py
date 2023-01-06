from django.shortcuts import render
from django.http import HttpResponse
menu_list = ['monitoring', 'map', 'log', 'store', 'person', 'login']
def menu(request):
    rez = '''<ul>
    '''
    for li in menu_list:
        rez += f'<li><a href="{li}">{li}</a></li>'
    rez += '</ul>'
    return HttpResponse(rez)

