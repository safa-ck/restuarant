from django.shortcuts import render
from web.models import Category,Dish


def index(request):
    category =Category.objects.all()
    dish =Dish.objects.all()
    return render(request, "index.html",{'category':category,'dish':dish})
# Create your views here.
