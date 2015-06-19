from django.shortcuts import render
from .models import Tree, FilterRequestObject
from django.core import serializers

from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.template import RequestContext
from .models import Tree
from TreeFinder.forms import FilterRequestObjectForm


# Create your views here.

def treefinder(request):
    context = RequestContext(request)
    treelist = Tree.objects.order_by("species")
    treelistJson = serializers.serialize("json", treelist)
    return render(request, 'TreeFinder/ahome.html', context)


def filter(request):
    # Get the context from the request.
    context = RequestContext(request)

    if request.method == 'POST':
        form = FilterRequestObjectForm(request.POST)
        #if we have a valid form, then save it to the db
        if form.is_valid():
            form.save(commit=True)
            f = FilterRequestObject.objects.all()[len(FilterRequestObject.objects.all()) - 1]

            neighborhood = f.Neighbourhood
            addr = f.Street
            height = f.HeightMin
            name = f.Species

            kwargDict = {
                'neighbourhoodName__iexact' : neighborhood ,
                'onStreet__iexact': addr,
                'heightRangeID__range': (height, 10),
                'species__iexact': name
            }

            if neighborhood == 'UNSPECIFIED':
                del kwargDict['neighbourhoodName__iexact']
            if addr == 'UNSPECIFIED':
                del kwargDict['onStreet__iexact']
            if height == 0:
                del kwargDict['heightRangeID__range']
            if name == 'UNSPECIFIED':
                del kwargDict['species__iexact']

            t = Tree.objects.all().filter(**kwargDict)
            tJson = serializers.serialize("json", t)

            for tree in t:
                print(tree.heightRangeID.__str__() + ' ' + tree.species + ' ' + tree.neighbourhoodName)

            return render(request, 'TreeFinder/ahome.html', {'Trees' : tJson})
        else:
            print(form.errors)
    else:
        # If the request was not a POST, display the form
        form = FilterRequestObjectForm()
    # Render the form
    return render_to_response('TreeFinder/ahome.html', {'form': form}, context)

