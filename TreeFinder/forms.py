from django.forms import ModelForm
from TreeFinder.models import FilterRequestObject

SPECIES_CHOICES = (
    ('SERRULATA', 'SERRULATA'),
    ('CONIFER', 'REDWOOD')
)


### filtering form code
class FilterRequestObjectForm(ModelForm):
    #CivicNumber = forms.ChoiceField()
    #OnStreet =
    # HeightRangeID =
    # Diameter =
    # GenusName =
    #SpeciesName = forms.ChoiceField(label = "Species", choices = SPECIES_CHOICES)
    # CommonName =
    class Meta:
         model = FilterRequestObject
         fields = ['Neighborhood', 'Street', 'HeightMin', 'CommonName']
