# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from eventex.core.models import Speaker
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
