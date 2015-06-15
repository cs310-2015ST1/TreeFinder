from django.shortcuts import render
from .models import Tree
from django.core import serializers

# Create your views here.

def treefinder(request):
    treelist = Tree.objects.order_by("species")[:10]
    treelistJson = serializers.serialize("json", treelist)
    return render(request, 'TreeFinder/home.html', {'Trees': treelistJson})