from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        #tn=request.POST['topic']
        tn=request.POST.get('topic')
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic is inseted successfully')

    return render(request,'insert_topic.html')

def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('Webpage is inserted se=uccessfully')
    return render(request,'insert_webpage.html',d)

def select_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        tn=request.POST.getlist('topic')
        print(tn)
        webpages=Webpage.objects.none()
        for i in tn:
            webpages=webpages|Webpage.objects.filter(topic_name=i)
        data={'webpages':webpages}
        return render(request,'display_webpage.html',data)
    return render(request,'select_topic.html',d)

def checkbox(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    
    return render(request,'checkbox.html',d)













