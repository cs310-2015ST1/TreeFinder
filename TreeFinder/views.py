from django.shortcuts import render, HttpResponse
from .models import Tree

# Create your views here.

def treefinder(request):
    treelist = Tree.objects.order_by("species")
    #return HttpResponse("Welcome to treefinder, where the trees are plenty!")
    return render(request, 'TreeFinder/home.html', {'Trees': treelist})