from django.shortcuts import render
from django.http import Http404


def pnr_status(request):
    try:
        di = {}
    except:
        raise Http404('request failure')
    return render(request, 'api/pnr_status.html', {'di': di})
