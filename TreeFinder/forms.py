from django.forms import ModelForm
from TreeFinder.models import FilterRequestObject


### filtering form code
class FilterRequestObjectForm(ModelForm):
    class Meta:
        model = FilterRequestObject
        fields = '__all__'


