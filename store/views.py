from django.shortcuts import render
from django.http import HttpResponse
def main(request):
    data = {
        'Title': 'Жулик',
        'Description': 'One ditch lalalal',
        'Date': '03.05.2020',
        'Time': '23:48',
        'Obj': ['Лукойл', 'Shell'],
    }
    response = render(request, 'store/info.html', context=data)
    return HttpResponse(response)

def get_note_info(request, note_id: int):
    data = {
        'Title': 'Жулик',
        'Description': 'One ditch lalalal',
        'Date': '03.05.2020',
        'Time': '23:48',
        'Obj': ['Лукойл', 'Shell'],
    }
    response = render(request, 'store/note_video.html', context=data)
    return HttpResponse(response)