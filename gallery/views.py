from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Photo
from .forms import PhotoForm
import os
from django.http import FileResponse, Http404
from django.conf import settings

# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,"gallery/register.html",{'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('gallery')
    else:
        form = AuthenticationForm()
    return render (request,'gallery/login.html',{'form':form})

def gallery(request):
    photos=Photo.objects.all().order_by('-uploaded_at')
    return render (request,'gallery/gallery.html',{'photos':photos})

@login_required
def upload(request):
    if request.method == 'POST':
        form=PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = PhotoForm()
    return render(request, 'gallery/upload.html', {'form': form})



@login_required
def protected_media(request, path):
    full_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.isfile(full_path):
        return FileResponse(open(full_path, 'rb'))
    raise Http404("File not found")




@login_required
def logout_view(request):
    logout(request)
    return redirect('gallery')
