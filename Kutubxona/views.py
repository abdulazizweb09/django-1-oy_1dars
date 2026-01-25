from django.shortcuts import render,redirect
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
    # if request=='POST':
    #     Talaba.objects.create(
    #         name=request.POST.get('name'),
    #         age=request.POST.get('age'),
    #         jins=request.POST.get('jins'),
    #         deta=request.POST.get('deta'),
    #         quantity=request.POST.get('quantity'),
    #         tric=request.POST.get('tric')
    #     )
    talaba=Talaba.objects.all()
    context={
        'talabalar':talaba
    }

    return render(request,'talaba.html',context)

def talaba_details(request,id):
    talaba=Talaba.objects.get(id=id)
    context={
        'talaba':talaba
    }
    return render(request,'talaba_details.html',context)

def kutubxonachi(request):
    kutubxona=Kutubxonachi.objects.all()
    context={
        'kutubxonachi':kutubxona
    }

    return render(request,'kutubxonachi.html',context)
def qoshish(request,type):
   
    if type == 'muallif' and request.method=='POST':
        tric=False
        if request.POST.get('tric')=='on':
            tric=True
        else:
            tric=False
        Muallif.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            jins=request.POST.get('jins'),
            quantity=request.POST.get('quant'),
            tric=tric,
        )
    elif type == 'talaba' and request.method=='POST':
        Talaba.objects.create(
            name=request.POST.get('name'),
            guruh=request.POST.get('guruh'),
            kurs=request.POST.get('kurs'),
            quantity=request.POST.get('quantity'),
        )
        redirect('/talaba')
        
        
        # FormClass = BookForm
        # pass
    elif type == 'record' and request.method=='POST' :

        Record.objects.create(
            talaba_id=request.POST.get('talaba'),
            kitob_id=request.POST.get('kitob'),
            admin_id=request.POST.get('admin'),
            olingan_sana=request.POST.get('olingan_sana'),
            qaytarish_sana=request.POST.get('qaytarish_sana'),
        )
        redirect('/talaba')

    elif type=='kutubxonachi' and request.method=='POST':
        Kutubxonachi.objects.create(
            name=request.POST.get('name'),
            start=request.POST.get('start'),
            end=request.POST.get('end')
        )
    # else:
    #     return redirect('/')

    # if request=='POST':
    context={
        'type':type,
        'muallif':Muallif.objects.all(),
        'talaba':Talaba.objects.all(),
        'kitob':Kitob.objects.all(),
        'admin':Kutubxonachi.objects.all()
    }
    return render(request,'qoshish.html',context)
