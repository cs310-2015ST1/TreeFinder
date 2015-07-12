"""
WSGI config for KnockOnWood project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, json

from django.db.transaction import atomic

from django.core.wsgi import get_wsgi_application

from TreeFinder.models import AddressMapping

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KnockOnWood.settings")

@atomic
def createMappings(pairs):
    for key in pairs:
        am = AddressMapping(address=key, x_coordinate=mappings[key]['latitude'], y_coordinate=mappings[key]['longitude'])
        am.save()

if len(AddressMapping.objects.all()) == 0:
    print("PARSING GEOCODE DATA")
    # json_data = open('/Users/gurneet_kalra_3/Development/cs310/TreeFinder/uploaded_files/westPointGrey.json')
    json_data = open(settings.BASE_DIR + '/uploaded_files/westPointGrey.json')
    mappings = json.load(json_data)
    json_data.close()
    createMappings(mappings)
    print("GEOCODE PARSING COMPLETE")


application = get_wsgi_application()