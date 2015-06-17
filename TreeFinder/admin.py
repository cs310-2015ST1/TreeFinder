from django.contrib import admin
from TreeFinder.models import Tree, TreeData, FilterRequestObject

# Register your models here.

class TreeAdmin(admin.ModelAdmin):
    list_display = ('species', 'neighbourhoodName', 'onStreet', 'onStreetBlock', 'heightRangeID', 'civicNumber')

class TreeDataAdmin(admin.ModelAdmin):
    list_display = ('file',)

class FilterRequestObjectAdmin(admin.ModelAdmin):
    list_display = ('SpeciesName','GenusName','CommonName', 'Diameter', 'OnStreet', 'HeightRangeID', 'CivicNumber')

admin.site.register(Tree, TreeAdmin)
admin.site.register(TreeData, TreeDataAdmin)
admin.site.register(FilterRequestObject, FilterRequestObjectAdmin)