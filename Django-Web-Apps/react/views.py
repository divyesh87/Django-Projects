from django.http.request import RAISE_ERROR
from django.http.response import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"react/index.html")

texts = ["lorem imdmfokdfi ij pvinewpoivnij vkjl eivnoernoe vk eiqcnqmcomoe", "helpoekmeoce j eofnioejfiojowicoiwenfonweoifnoienf", 
"uwqkdweoioew dojewnoiewjimco dec oenfiejfomxko dnwednd9n"]

def loadsection(request,section):
    if section>=1 and section<=3:
        return HttpResponse(texts[section-1])
    else:
        raise Http404("No such section")

def scroll(request):
    return render(request,"react/scroll.html")