from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import get_template
from articles.models import Articles
# Create your views here.
from django.template.response import TemplateResponse
from django.views.generic import ListView

class ArticlesList(ListView):
    model = Articles

def start(request):
    articles=Articles.objects.all()
    response=TemplateResponse(request,'lots.html',locals())
    return response

def lot(request,num):
    numb=num
    try:
        lot=Articles.objects.get(id=num)
    except:
        return redirect('../../')
    response=TemplateResponse(request,'lot.html',locals())
    return response