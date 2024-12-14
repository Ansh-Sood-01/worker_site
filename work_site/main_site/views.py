from django.shortcuts import render

from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def showcase(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    return render(request,'showcase_your_work.html' , {"categories": categories, "images": images})

def browse_workers(request):
    categories = Category.objects.all()
    workers = Worker.objects.all()

    # Filter workers by category if a category filter is applied
    category_filter = request.GET.get('category')
    if category_filter:
        workers = workers.filter(category__name=category_filter)

    context = {
        'categories': categories,
        'workers': workers,
    }
    return render(request,'browse_workers.html', context)