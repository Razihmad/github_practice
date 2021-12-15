from django.shortcuts import render
from app.models import FileModel
# Create your views here.
def home(request):
    if request.method=='POST':
        file = request.FILES['file']
        f = FileModel(file=file)
        f.save()

    return render(request,'home.html')