from django.shortcuts import render
from .models import *
# Create your views here.
def ustoz(request):

    ustoz=Ustoz.objects.all()
    fan=Fan.objects.all()
    context={
        'ustoz':ustoz,
        'fan':fan
    }

    return render(request,'ustoz.html',context)

def yonalish(request):

    yonalish=Yonalish.objects.all()

    context={
        'yonalish':yonalish,
    }

    return render(request,'yonalish.html',context)

def fan(request):

    fan=Fan.objects.all()
    context={
        'fan':fan,
    }

    return render(request,'fan.html',context)