from django.contrib import admin
from TreeFinder.models import Tree, TreeData

# Register your models here.

class TreeAdmin(admin.ModelAdmin):
    list_display = ('species', 'neighbourhoodName', 'onStreet', 'onStreetBlock', 'heightRangeID', 'civicNumber')

class TreeDataAdmin(admin.ModelAdmin):
    list_display = ('file',)

admin.site.register(Tree, TreeAdmin)
admin.site.register(TreeData, TreeDataAdmin)