from django.shortcuts import render
import logging
# Create your views here.
from .forms import StudentForm
from django.http import HttpResponse
def index(request):
    if request.method=="POST":
        fm=StudentForm(request.POST)

    else :
        fm=StudentForm()

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    a='%(asctime)s'+"--"+ip+request.method+ str(request.user)+"   "+'%(name)s'
    logging.basicConfig(filename='logged1.log',format=a)
    return render(request,'app/index.html',{'form':fm})