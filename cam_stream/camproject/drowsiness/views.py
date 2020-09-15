from django.shortcuts import render, redirect
from django.http import HttpResponse
import drow.tts as tts
from django.http import FileResponse
from django.conf import settings
import os, mimetypes
from .models import Sound

# Create your views here. 
def home(request): # 의미 없는 path 입니다. 신경 쓰지 마세요.
    return HttpResponse('Hello')

def setting(request): # 알람을 만드는 부분 입니다.
    if request.method == 'GET' :
        return render(request, 'chat/setting.html',{})
    elif request.method == 'POST':
        content = request.POST['sound-content-input']
        name = tts.make_tts(content,'alarm2')
        return HttpResponse(name)

def alarm(request):
    if request.method == 'GET':
        # print(settings.BASE_DIR)
        context = {
            'results' : Sound.objects.get(title='alarm')
        }
        return render(request, 'alarm.html',context)

def media(request):
    if request.method=='GET':
        return render(request, 'media.html', {})
    else:
        file = request.FILES['sori']
        Sound.objects.create(
            title = 'alarm',
            alarm = file
        )

        return redirect('media')

    
def room(request, room_name):
    return render(request, 'chat/room.html',{
        'room_name':room_name
    })

def media_serve(request, name):
    print('hi',name)
    file_path = os.path.join(settings.BASE_DIR, name)
    print('hi',file_path)
    return FileResponse(open(file_path, 'rb'), content_type=mimetypes.guess_type(file_path)[0])