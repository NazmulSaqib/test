from django.shortcuts import render
from .forms import PhotoForm
from .models import Photo

# Create your views here.

def home(request):
    if request.method == 'POST':
        form =PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = PhotoForm()
    photos = Photo.objects.all()
    return render(request, 'myapp/home.html', {'form':form, 'photos':photos})
