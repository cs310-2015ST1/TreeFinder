<<<<<<< Updated upstream
from django.shortcuts import render
from .models import Tree
from django.core import serializers
=======
from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.template import RequestContext
from .models import Tree
from TreeFinder.forms import FilterRequestObjectForm
>>>>>>> Stashed changes

# Create your views here.

def treefinder(request):
<<<<<<< Updated upstream
    treelist = Tree.objects.order_by("species")[:10]
    treelistJson = serializers.serialize("json", treelist)
    return render(request, 'TreeFinder/home.html', {'Trees': treelistJson})
=======
    treelist = Tree.objects.order_by("species")
    #return HttpResponse("Welcome to treefinder, where the trees are plenty!")
    return render(request, 'TreeFinder/home.html', {'Trees': treelist})


def filter(request):
    # Get the context from the request.
    context = RequestContext(request)

    if request.method == 'POST':
        form = FilterRequestObjectForm(request.POST)
        #if we have a valid form, then save it to the db
        if form.is_valid():
            form.save(commit=True)
            return treefinder(request)
        else:
            print(form.errors)
    else:
        # If the request was not a POST, display the form
        form = FilterRequestObjectForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('TreeFinder/filter.html', {'form': form}, context)
>>>>>>> Stashed changes
