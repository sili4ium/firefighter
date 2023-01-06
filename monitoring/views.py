from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

stations = {
    'Obj-A': ['Area-1', 'Area-2'],
    'Obj-B': ['Area-3', 'Area-4'],
}

datadata = {
    'Obj-AArea-1': ['https://in-bez.ru/upload/medialibrary/f2e/f2e202425573920f3edfb9df999f8a13.jpg', (0, 0, 1)],
    'Obj-AArea-2': ['https://www.secnews.ru/upload/iblock/pr/01/ISS-lukoil-1.jpg', (0, 0, 0)],
    'Obj-BArea-3': ['https://se-cam.ru/image/data/A-setka/551a7ff64efff.jpg', (0, 0, 0)],
    'Obj-BArea-4': ['https://img.youtube.com/vi/EbgmKa6_-6A/0.jpg', (1, 2, 0)],
}

def get_area_info(request, obj: str, area: str):
    param_k = str(obj + area)
    param_v = datadata[param_k]
    video_url = param_v[0]
    params = []
    for p in param_v[1]:
        if p == 0:
            params.append(f'<span style="color: green;">Норма</span>')
        elif p == 1:
            params.append(f'<span style="color: red;">Превышение,<br>норма <strong>123</strong>,<br>фактически <strong>123</strong></span>')
        else:
            params.append(f'<span style="color: yellow;">Ошибка,<br>норма <strong>123</strong>,<br>фактически <strong>123</strong></span>')
    data = {
        'dict': stations,
        'stations': list(stations.keys()),
        'stat': obj,
        'area': area,
        'v_url': video_url,
        'params': params
    }
    response = render(request, 'monitoring/info.html', context=data)
    return HttpResponse(response)
    # if stat and area in stat:
    #     return HttpResponse(f'{obj}{area}')
    # else:
    #     return HttpResponseNotFound(f"Error")



def no_area_info(request):
    first_args = list(list(stations.items())[0])
    redirect_url = reverse('monitor', args=(first_args[0], first_args[1][0]))
    return HttpResponseRedirect(redirect_url)
