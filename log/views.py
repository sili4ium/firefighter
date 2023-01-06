from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
ev = {
    1: ['ol'],
    2: ['eve']
}

def main(request):
    params = []
    for p in (-1, 0, 0):
        if p == 0:
            params.append(f'<span style="color: green;">Норма</span>')
        elif p == 1:
            params.append(
                f'<span style="color: red;">Превышение,<br>норма <strong>123</strong>,<br>фактически <strong>123</strong></span>')
        else:
            params.append(
                f'<span style="color: yellow;">Ошибка,<br>норма <strong>123</strong>,<br>фактически <strong>123</strong></span>')
    data = {
        'Type_f': 'Третье',
        'Type_code_f': 'third',
        'Type_s': 'Четвертое',
        'Type_code_s': 'fourth',
        'Obj': 'Заправка Ева',
        'Date': '03.05.2020',
        'Time': '23:48',
        'Objj': 'Лукойл',
        'Area': '354',
        'Type': 'Лужа',
        'params': params,
    }
    response = render(request, 'log/info.html', context=data)
    return HttpResponse(response)

def get_ev(request, ev_id:int):
    params = []
    for p in (-1, 0, 0):
        if p == 0:
            params.append(f'<span style="color: green;">Норма</span>')
        elif p == 1:
            params.append(
                f'<span style="color: red;">Превышение,<br>норма <strong>123</strong>,<br>фактически <strong>123</strong></span>')
        else:
            params.append(
                f'<span style="color: yellow;">Ошибка,<br>норма <strong>123</strong>,<br>фактически <strong>123</strong></span>')
    data = {
        'Type_f': 'Третье',
        'Type_code_f': 'third',
        'Type_s': 'Четвертое',
        'Type_code_s': 'fourth',
        'Obj': 'Заправка Ева',
        'Date': '03.05.2020',
        'Time': '23:48',
        'Objj': 'Лукойл',
        'Area': '354',
        'Type': 'Лужа',
        'params': params,
    }
    response = render(request, 'log/event.html', context=data)
    return HttpResponse(response)

