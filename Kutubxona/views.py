from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):

    mualliflar=Muallif.objects.all()
    context={
        'mualliflar':mualliflar
    }

    return render(request,'index.html',context)


def details(request,id):

    muallif=Muallif.objects.get(id=id)
    # print(muallif)
    context={
        'muallif':muallif
    }

    return render(request,'details.html',context)

def kitoblar(request):
    kitoblar=Kitob.objects.all()
    # print(kitob)
    context={
        'kitoblar':kitoblar
    }
    return render(request,'kitob.html',context)

def kitob(request,id):
    kitob=Kitob.objects.get(id=id)
    context={
        'kitob':kitob
    }
    return render(request,'kitob_details.html',context)

def record(request):
    record=Record.objects.all()
    print(record)
    context={
        'record':record
    }
    return render(request,'record.html',context)

def talaba(request):
    talaba=Talaba.objects.all()
    context={
        'talaba':talaba
    }

    return render(request,'talaba.html',context)