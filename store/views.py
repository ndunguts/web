from django.shortcuts import render
from . models import Movies,tv


# Create your views here.
def add(request):
    movies = Movies.objects.all()
    channe= tv.objects.all()
    return render(request,"home1.html",{'movi':movies , 'chann':channe})
