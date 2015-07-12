from django.shortcuts import render
from .models import Tree, FilterRequestObject
from django.core import serializers

from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.template import RequestContext
from .models import Tree
from TreeFinder.forms import FilterRequestObjectForm, UserForm, UserProfileForm


# Create your views here.

def treefinder(request):
    context = RequestContext(request)
    treelist = Tree.objects.order_by("species")
    treelistJson = serializers.serialize("json", treelist)
    return render(request, 'TreeFinder/home.html', {'Trees': treelistJson})

def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'TreeFinder/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

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

            return render(request, 'TreeFinder/home.html', {'Trees' : tJson})
        else:
            print(form.errors)
    else:
        # If the request was not a POST, display the form
        form = FilterRequestObjectForm()
    # Render the form
    return render_to_response('TreeFinder/home.html', {'form': form}, context)

