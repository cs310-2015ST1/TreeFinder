from django.shortcuts import render
from .models import Tree, FilterRequestObject
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, render_to_response
from django.template import RequestContext
from .models import Tree
from TreeFinder.forms import FilterRequestObjectForm, UserForm, UserProfileForm, PasswordForm
from django.contrib.auth.decorators import login_required
import json

# Create your views here.

def treefinder(request):
    kwargDict = {
        'species__iexact': "WESTERN RED CEDAR"
    }
    treeUserMappings = {}
    t = Tree.objects.all().filter(**kwargDict)
    for tree in t:
        treeUserMappings[str(tree.pk)] = []
        if len(tree.userprofile_set.all()) == 0:
            treeUserMappings[str(tree.pk)].append("")
        for userprofile in tree.userprofile_set.all():
            treeUserMappings[str(tree.pk)].append(str(userprofile.user.username))
    tJson = serializers.serialize("json", t)
    treeUserMappingsJson = json.dumps(treeUserMappings)

    return render(request, 'TreeFinder/home.html', {'Trees' : tJson, 'treeUserMappings' : treeUserMappingsJson})


def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('templates/home.html',
                             context_instance=context)


def filter(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = FilterRequestObjectForm(request.POST)

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

            treeUserMappings = {}
            t = Tree.objects.all().filter(**kwargDict)
            for tree in t:
                treeUserMappings[str(tree.pk)] = []
                if len(tree.userprofile_set.all()) == 0:
                    treeUserMappings[str(tree.pk)].append("")
                for userprofile in tree.userprofile_set.all():
                    treeUserMappings[str(tree.pk)].append(str(userprofile.user.username))
            tJson = serializers.serialize("json", t)
            treeUserMappingsJson = json.dumps(treeUserMappings)

            for tree in t:
                print(tree.heightRangeID.__str__() + ' ' + tree.species + ' ' + tree.neighbourhoodName)

            return render(request, 'TreeFinder/home.html', {'Trees' : tJson, 'treeUserMappings' : treeUserMappingsJson})
        else:
            print(form.errors)
    else:
        form = FilterRequestObjectForm()
    return render_to_response('TreeFinder/home.html', {'form': form}, context)



def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'TreeFinder/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your TreeFinder account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'TreeFinder/login.html', {})


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/')




@login_required
def profile(request):
    trees = request.user.userprofile.treelist.all()
    if request.method == 'POST':
        password = request.POST.get('password')
        user = request.user.userprofile.user
        user.set_password(password)
        user.save()
        return render(request, 'TreeFinder/profile.html', {"trees":trees})
    else:
        return render(request,'TreeFinder/profile.html', {"trees":trees, 'password_form': PasswordForm,})



@login_required
def addTreeToTreeList(request):
    print("view function addTreeToTreeList called")
    jsondata = request.body
    print(request.body)
    tree = json.loads(jsondata.decode('utf-8') )
    print(tree["ID"])
    # some magic that gives us the proper tree with respect to the requested json format tree string
    theMoneyShot = Tree.objects.get(id=tree["ID"])
    request.user.userprofile.treelist.add(theMoneyShot)

    return HttpResponse("yoi tuy retyu")

