from django.shortcuts import render
from .models import Uploader
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        tittle = request.POST['tittle']
        desc = request.POST['desc']
        image = request.FILES['img']
        obj = Uploader.objects.create(tittle=tittle,desc =desc,image=image)
        messages.success(request,"Image Uploaded!")
        obj.save()
    
    data = Uploader.objects.all()
    return render(request,'main/base.html',{'data':data})

