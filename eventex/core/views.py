# coding: utf-8

#from datetime import time
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from eventex.core.models import Speaker, Talk
#from django.http import HttpResponse

def homepage(request):
    return render(request, 'index.html')

'''
def speaker_detail(request, slug):
    return HttpResponse()
'''
'''    
def speaker_detail(request, slug):
    return render(request, 'core/speaker_detail.html')
'''

def speaker_detail(request, slug):
#    context = {'speaker': Speaker()}
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html',
        context)
'''        
def talk_list(request):
    from django.http import HttpResponse
    return HttpResponse()
'''
'''
def talk_list(request):
    return render(request, 'core/talk_list.html')
'''
    
def talk_list(request):
#    midday = time(12)
    context = {
#        'morning_talks': Talk.objects.filter(start_time__lt=midday),
#        'afternoon_talks': Talk.objects.filter(start_time__gte=midday),
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
        }
    return render(request, 'core/talk_list.html', context)
'''    refatorado pagina 239 aula 4    
def talk_detail(request, pk):
    talk = get_object_or_404(Talk, pk=pk)
    context = {
        'talk': talk,
        'slides': talk.media_set.filter(kind='SL'),
        'videos': talk.media_set.filter(kind='YT'),
    }
    return render(request, 'core/talk_detail.html', context)
'''
def talk_detail(request, pk):
    talk = get_object_or_404(Talk, pk=pk)
    context = {
        'talk': talk,
    }
    return render(request, 'core/talk_detail.html', context)
    
    