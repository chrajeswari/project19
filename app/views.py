from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QLAO=AccessRecord.objects.all()
    d={'access':QLAO}
    return render(request,'display_access.html',d)




def insert_topic(request):
    tn=input('enter topic_name')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()

    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)




def insert_webpage(request):
    tn=input('enter topic_name')
    n=input('enter name')
    u=input('enter url')
    to=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    NWO.save()

    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',d)




def insert_access(request):
    pk=int(input('enter pk value of wabpage'))
    a=input('enter author')
    d=input('enter date')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()

    QLAO=AccessRecord.objects.all()
    d={'access':QLAO}
    return render(request,'display_access.html',d)



   