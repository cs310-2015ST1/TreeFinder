from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
from django.conf import settings
from xml.etree import ElementTree
from django.contrib.auth.models import User
from django.db.transaction import atomic

UPLOAD_DIRECTORY = '/uploaded_files/'
FULL_UPLOAD_PATH = settings.BASE_DIR + UPLOAD_DIRECTORY

fss = FileSystemStorage(location=FULL_UPLOAD_PATH)

# Create your models here.
class Location(models.Model):
    x_coordinate = models.FloatField(default=0.0)
    y_coordinate = models.FloatField(default=0.0)


class Tree(models.Model):

    # rating = models.FloatField(default=0.0)
    # ratingcount = models.IntegerField(default=0.0)

    species = models.CharField(max_length=200)
    neighbourhoodName = models.CharField(max_length=200, default='UNSPECIFIED')
    cell = models.IntegerField(default=0)
    onStreet = models.CharField(max_length=200, default='UNSPECIFIED')
    onStreetBlock = models.IntegerField(default=0)
    heightRangeID = models.IntegerField(default=0)
    civicNumber = models.IntegerField(default=0)
    x_coordinate = models.FloatField(default=0.0)
    y_coordinate = models.FloatField(default=0.0)
    # location = models.ForeignKey(Location)
    def __str__(self):  # __unicode__ on Python 2
        return self.species

    # def rateTree(self, rating):
    #     totalscore = self.rating * self.ratingcount
    #     self.ratingcount += 1
    #     totalscore = totalscore + rating
    #     self.rating = totalscore / self.ratingcount

class UserProfile(models.Model):
    # Makes a tree list
    treelist = models.ManyToManyField(Tree)
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # additional attributes we wish to include.
    website = models.URLField(blank=True)

     # Override the __unicode__() method to return out something meaningful
    def __str__(self):
        return self.user.username


class TreeData(models.Model):
    file = models.FileField(verbose_name='Filename', storage=fss, default='xml data file')
    uploadedFile = None

    @staticmethod
    def parse(xml_file):
        root = ElementTree.fromstring(xml_file.read())
        parsedData = []
        for streetTree in root.iter("StreetTree"):
            thisTree = {}
            thisTree['onStreet'] = streetTree.find('OnStreet').text
            thisTree['onStreetBlock'] = streetTree.find('OnStreetBlock').text
            thisTree['civicNumber'] = streetTree.find('CivicNumber').text
            thisTree['address'] = str(thisTree['civicNumber']) + " " + thisTree['onStreet'] + ", Vancouver, Canada"
            thisTree['commonName'] = streetTree.find('CommonName').text
            thisTree['neighbourhoodName'] = streetTree.find('NeighbourhoodName').text
            thisTree['cell'] = streetTree.find('Cell').text
            thisTree['heightRangeID'] = streetTree.find('HeightRangeID').text
            parsedData.append(thisTree)
        return parsedData

    @staticmethod
    @atomic
    def createTrees(parsedTreeData):
        for tree in parsedTreeData:
            print("STARTING LOOKUP")
            print(tree['address'])
            try:
                addressMap = AddressMapping.objects.get(address=tree['address'])
                # print("COORDINATES: ")

                t = (Tree(species=tree['commonName'],
                          neighbourhoodName=tree['neighbourhoodName'],
                          cell=tree['cell'],
                          onStreet=tree['onStreet'],
                          onStreetBlock=tree['onStreetBlock'],
                          heightRangeID=tree['heightRangeID'],
                          civicNumber=tree['civicNumber'],
                          x_coordinate=addressMap.x_coordinate,
                          y_coordinate=addressMap.y_coordinate
                          ))
                t.save()

            except AddressMapping.DoesNotExist:
                print("MAPPING FAILURE")

    def save(self, *args, **kwargs):
        super(TreeData, self).save(*args, **kwargs)
        uploadedFile = UploadedFile(file=self.file, name='test')
        TreeData.createTrees(TreeData.parse(uploadedFile))


### Filtering code

class FilterRequestObject(models.Model):
    filter = models.ForeignKey('Tree', blank=True, null=True, unique=False)
    Neighbourhood = models.CharField(max_length=200, default='UNSPECIFIED')
    Street = models.CharField(max_length=200, default='UNSPECIFIED')
    HeightMin = models.IntegerField(default=0)
    Species = models.CharField(max_length=200, default='UNSPECIFIED')

    # populates filteredlist with Trees meeting filterlogic criteria
    def populateFilteredList(self):

        name = self.Species
        addr = self.Street
        neighborhood = self.Neighbourhood
        height = self.HeightMin

        kwargDict = {
            'neighbourhoodName__iexact': neighborhood,
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

        t = Tree.objects.all()

        filter = t.filter(**kwargDict)
        for tree in filter:
            print(tree.species + tree.neighbourhoodName + tree.heightRangeID.__str__())

    def save(self, *args, **kwargs):
        self.populateFilteredList()
        super(FilterRequestObject, self).save(*args, **kwargs)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class FilteredTree(models.Model):
    species = models.CharField(max_length=200)
    neighbourhoodName = models.CharField(max_length=200, default='UNSPECIFIED')
    cell = models.IntegerField(default=0)
    onStreet = models.CharField(max_length=200, default='UNSPECIFIED')
    onStreetBlock = models.IntegerField(default=0)
    heightRangeID = models.IntegerField(default=0)
    civicNumber = models.IntegerField(default=0)
    # location = models.ForeignKey(Location)
    def __str__(self):  # __unicode__ on Python 2
        return self.species


class AddressMapping(models.Model):
    address = models.CharField(max_length=300, unique=True)
    x_coordinate = models.FloatField(default=0.0)
    y_coordinate = models.FloatField(default=0.0)

    def __str__(self):
        return self.address
