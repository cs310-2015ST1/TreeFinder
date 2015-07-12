__author__ = 'gurneet_kalra_3'

from django.contrib import admin
from TreeFinder.models import Tree, TreeData, FilterRequestObject, AddressMapping, UserProfile


# Register your models here.

class TreeAdmin(admin.ModelAdmin):
    list_display = ('species', 'neighbourhoodName', 'onStreet', 'onStreetBlock', 'heightRangeID', 'civicNumber',
                    'x_coordinate', 'y_coordinate')

class TreeDataAdmin(admin.ModelAdmin):
    list_display = ('file',)

class FilterRequestObjectAdmin(admin.ModelAdmin):
    list_display = ('Neighbourhood', 'Street', 'HeightMin', 'Species')

class AddressMappingAdmin(admin.ModelAdmin):
    list_display = ('address', 'x_coordinate', 'y_coordinate')

admin.site.register(Tree, TreeAdmin)
admin.site.register(TreeData, TreeDataAdmin)
admin.site.register(FilterRequestObject, FilterRequestObjectAdmin)
admin.site.register(AddressMapping, AddressMappingAdmin)
admin.site.register(UserProfile)