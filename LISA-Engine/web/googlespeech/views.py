from django.http import HttpResponse
from django.shortcuts import render
try:
    from web.lisa.settings import configuration
except ImportError:
    from lisa.settings import configuration

def index(request):
    if configuration['enable_secure_mode']:
        websocket = 'wss'
    else:
        websocket = 'ws'
    context = {'websocket': websocket}
    return render(request, 'googlespeech/index.html', context)
