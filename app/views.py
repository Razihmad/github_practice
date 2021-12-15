from django.http.request import HttpRequest
from django.shortcuts import render,HttpResponse
from app.models import FileModel
# Create your views here.
def home(request):
    if request.method=='POST':
        file = request.FILES['file']
        f = FileModel(file=file)
        f.save()

    return render(request,'home.html')


def ra(request):
    return HttpResponse('nothing to be worried')


def testing(request):
    return HttpResponse('workign tree clean not possible')

