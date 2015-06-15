from django.forms import ModelForm, Form
from TreeFinder.models import FilterRequestObject


### filtering form code
class FilterRequestObjectForm(ModelForm):
    # CivicNumber = form
    # OnStreet =
    # HeightRangeID =
    # Diameter =
    # GenusName =
    # SpeciesName =
    # CommonName =
    class Meta:
        model = FilterRequestObject
        fields = '__all__'


