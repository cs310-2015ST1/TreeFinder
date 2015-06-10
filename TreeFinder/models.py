from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
from django.conf import settings
from xml.etree import ElementTree

UPLOAD_DIRECTORY = '/uploaded_files/'
FULL_UPLOAD_PATH = settings.BASE_DIR + UPLOAD_DIRECTORY
XML_SPECIES = 'SpeciesName'

fss = FileSystemStorage(location=FULL_UPLOAD_PATH)

# Create your models here.
class Location(models.Model):
    x_coordinate = models.FloatField(default=0.0)
    y_coordinate = models.FloatField(default=0.0)

class Tree(models.Model):
    species = models.CharField(max_length=200)
    #location = models.ForeignKey(Location)

class TreeData(models.Model):
    file = models.FileField(verbose_name='Filename', storage=fss, default='xml data file')
    uploadedFile = None
    allSpecies = []

    def parseIntoModel(self, xml_file):
        root = ElementTree.fromstring(xml_file.read())
        for species in root.iter(XML_SPECIES):
                self.allSpecies.append(species)
        print("TOTAL NUMBER OF SPECIES ENTRIES = " + str(len(self.allSpecies)))

    def save(self, *args, **kwargs):
        super(TreeData, self).save(*args, **kwargs)
        uploadedFile = UploadedFile(file=self.file, name='test')
        self.parseIntoModel(uploadedFile)