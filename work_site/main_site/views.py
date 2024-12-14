from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def showcase(request):
    return render(request,'showcase_your_work.html')

def browse_workers(request):
    return render(request,'browse_workers.html')