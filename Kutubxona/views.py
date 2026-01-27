from django.shortcuts import render,redirect
from .models import *
from Universitet.models import *
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

def records(request,id):
    record=Record.objects.get(id=id)
    context={
        'record':record
    }
    return render(request,'reacord_details.html',context)


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
        return redirect('/talaba')
        
        
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
        return redirect('/record')

    elif type=='kutubxonachi' and request.method=='POST':
        Kutubxonachi.objects.create(
            name=request.POST.get('name'),
            start=request.POST.get('start'),
            end=request.POST.get('end')
        )
        return redirect('/kutubxonachi')

    elif type=='ustoz' and request.method=='POST':
        Ustoz.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            jins=request.POST.get('jins'),
            daraja=request.POST.get('daraja'),
            fan_id=request.POST.get('fan'),
        )
        return redirect('/ustoz')

    elif type=='yonalish' and request.method=='POST':
        activ=False
        if request.POST.get('activ')=='on':
            activ=True
        else:
            activ=False
        Yonalish.objects.create(
            name=request.POST.get('name'),
            activ=activ
        )
        return redirect('/yonalish')

    elif type=='fan' and request.method=='POST':
        activ=False
        if request.POST.get('activ')=='on':
            activ=True
        else:
            activ=False
        idd=request.POST.get('yonalish')
        yonalish=Yonalish.objects.get(id=idd)
        Fan.objects.create(
            name=request.POST.get('name'),
            asosiy=activ,
            yonalish=yonalish
        )
        return redirect('/fan')

    # else:
    #     return redirect('/')

    # if request=='POST':
    context={
        'type':type,
        'muallif':Muallif.objects.all(),
        'talaba':Talaba.objects.all(),
        'kitob':Kitob.objects.all(),
        'admin':Kutubxonachi.objects.all(),
        'yonalish':Yonalish.objects.all(),
        'fan':Fan.objects.all(),
        'ustoz':Ustoz.objects.all(),
    }
    return render(request,'qoshish.html',context)
