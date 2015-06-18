from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
from django.conf import settings
from xml.etree import ElementTree

UPLOAD_DIRECTORY = '/uploaded_files/'
FULL_UPLOAD_PATH = settings.BASE_DIR + UPLOAD_DIRECTORY

fss = FileSystemStorage(location=FULL_UPLOAD_PATH)

# Create your models here.
class Location(models.Model):
    x_coordinate = models.FloatField(default=0.0)
    y_coordinate = models.FloatField(default=0.0)


class Tree(models.Model):
    species = models.CharField(max_length=200)
    neighbourhoodName = models.CharField(max_length=200, default='UNSPECIFIED')
    cell = models.IntegerField(default=0)
    onStreet = models.CharField(max_length=200, default='UNSPECIFIED')
    onStreetBlock = models.IntegerField(default=0)
    heightRangeID = models.IntegerField(default=0)
    civicNumber = models.IntegerField(default=0)
    # location = models.ForeignKey(Location)


class TreeData(models.Model):
    file = models.FileField(verbose_name='Filename', storage=fss, default='xml data file')
    uploadedFile = None

    def parseIntoModel(self, xml_file):
        root = ElementTree.fromstring(xml_file.read())
        for streetTree in root.iter("StreetTree"):  # StreetTree is the name in the XML file
            # Construct a new Tree entry in our models for each StreetTree in the file
            t = (Tree(species=streetTree.find('CommonName').text,
                      neighbourhoodName = streetTree.find('NeighbourhoodName').text,
                      cell = streetTree.find('Cell').text,
                      onStreet = streetTree.find('OnStreet').text,
                      onStreetBlock = streetTree.find('OnStreetBlock').text,
                      heightRangeID = streetTree.find('HeightRangeID').text,
                      civicNumber = streetTree.find('CivicNumber').text))

            t.save()

    def save(self, *args, **kwargs):
        super(TreeData, self).save(*args, **kwargs)
        uploadedFile = UploadedFile(file=self.file, name='test')
        self.parseIntoModel(uploadedFile)





### Filtering code

class FilterRequestObject(models.Model):

    filter = models.ForeignKey('Tree', blank = True, null = True, unique = False)
    Neighbourhood = models.CharField(max_length=200, default='UNSPECIFIED')
    Street = models.CharField(max_length=200, default='UNSPECIFIED')
    HeightMin = models.IntegerField(default = 0)
    Species = models.CharField(max_length=200, default='UNSPECIFIED')

     # populates filteredlist with Trees meeting filterlogic criteria
    def populateFilteredList(self):

        name = self.Species
        addr = self.Street
        neighborhood = self.Neighbourhood
        height = self.HeightMin

        kwargDict = {
            'neighbourhoodName__iexact' : neighborhood ,
            'onStreet__iexact': addr,
            'heightrangeid__range': (height, 10),
            'species__iexact': name
        }

        if neighborhood == 'UNSPECIFIED':
            del kwargDict['neighbourhoodName__iexact']
        if addr == 'UNSPECIFIED':
            del kwargDict['onStreet__iexact']
        if height == 0:
            del kwargDict['heightrangeid__range']
        if name == 'UNSPECIFIED':
            del kwargDict['species__iexact']

        t = Tree.objects.all()

        filter = t.filter(kwargDict)
        for t in filter:
            print(t.species)



    def save(self, *args, **kwargs):
        self.populateFilteredList()
        super(FilterRequestObject, self).save(*args, **kwargs)

    def __str__(self):              # __unicode__ on Python 2
        return self.name



