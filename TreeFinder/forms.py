from django import forms
from django.forms import ModelForm
from TreeFinder.models import FilterRequestObject

SPECIES_CHOICES = (
    ('NORWAY MAPLE', 'NORWAY MAPLE'),
    ('CONIFER', 'REDWOOD')
)

HEIGHT_CHOICES = (
    (1 , 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
)

NEIGHBOURHOOD_CHOICES = (
    ('KITSILANO', 'Kitsilano'),
    ('POINT GREY', 'Point Grey'),
    ('FAIRVIEW', 'Fairview')
)

### filtering form code
class FilterRequestObjectForm(ModelForm):
    Species = forms.ChoiceField(label = "Species", choices = SPECIES_CHOICES)
    Neighbourhood = forms.ChoiceField(label = "Neighbourhood to Search", choices = NEIGHBOURHOOD_CHOICES)
    HeightMin = forms.ChoiceField(label = "Minimum Height", choices = HEIGHT_CHOICES)
    class Meta:
         model = FilterRequestObject
         fields = ['Neighbourhood', 'HeightMin', 'Species']
