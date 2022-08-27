from django.http.response import JsonResponse
from django.shortcuts import render
import time

# Create your views here.
 

def index(request):
    return render(request, "scroll/index.html")

def loadpost(request):
    start = int(request.GET.get("start") or 0)
    end  = int(request.GET.get("end") or 9)

    data = []
    for i in range (start, end + 1):
        data.append(f"post #{i}")

    time.sleep(1)

    return JsonResponse({'posts' : data},safe=False)
