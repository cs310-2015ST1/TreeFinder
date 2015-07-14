from django.test import TestCase
from .models import TreeData

# Create your tests here.

PATH = 'test_files/'
ONE_TREE = PATH+'oneTree.xml'
TWO_TREES = PATH+'twoTrees.xml'
TEN_TREES = PATH+'tenTrees.xml'
MANY_TREES = PATH+'manyTrees.xml'
MISSING = PATH+'oneTreeMissingFields.xml'

class ParserTest(TestCase):

    def testParseOneTree(self):
        file = open(name=ONE_TREE)
        parsedData = TreeData.parse(file)
        self.assertEqual(len(parsedData), 1)
        file.close()

    def testParseTwoTrees(self):
        file = open(name=TWO_TREES)
        parsedData = TreeData.parse(file)
        self.assertEqual(len(parsedData), 2)
        file.close()

    def testParseTenTrees(self):
        file = open(name=TEN_TREES)
        parsedData = TreeData.parse(file)
        self.assertEqual(len(parsedData), 10)
        file.close()

    def testParseThousandsOfTrees(self):
        file = open(name=MANY_TREES)
        parsedData = TreeData.parse(file)
        self.assertEqual(len(parsedData), 4843)
        file.close()

    def testExtractProperty(self):
        file = open(name=ONE_TREE)
        parsedData = TreeData.parse(file)
        assert('civicNumber' in parsedData[0])
        self.assertEqual(parsedData[0]['civicNumber'], '4694')
        file.close()

    def testExtractTwoProperties(self):
        file = open(name=ONE_TREE)
        parsedData = TreeData.parse(file)
        assert('onStreet' in parsedData[0])
        assert('heightRangeID' in parsedData[0])
        self.assertEqual(parsedData[0]['onStreet'], 'BLANCA ST')
        self.assertEqual(parsedData[0]['heightRangeID'], '5')
        file.close()

    def testExtractManyProperties(self):
        file = open(name=ONE_TREE)
        parsedData = TreeData.parse(file)
        assert('onStreet' in parsedData[0])
        assert('onStreetBlock' in parsedData[0])
        assert('civicNumber' in parsedData[0])
        assert('address' in parsedData[0])
        assert('commonName' in parsedData[0])
        assert('neighbourhoodName' in parsedData[0])
        assert('cell' in parsedData[0])
        assert('heightRangeID' in parsedData[0])
        self.assertEqual(parsedData[0]['onStreet'], 'BLANCA ST')
        self.assertEqual(parsedData[0]['onStreetBlock'], '2400')
        self.assertEqual(parsedData[0]['civicNumber'], '4694')
        self.assertEqual(parsedData[0]['address'], '4694 BLANCA ST, Vancouver, Canada')
        self.assertEqual(parsedData[0]['commonName'], 'SPECKLED ALDER')
        self.assertEqual(parsedData[0]['neighbourhoodName'], 'WEST POINT GREY')
        self.assertEqual(parsedData[0]['cell'], '12')
        self.assertEqual(parsedData[0]['heightRangeID'], '5')
        file.close()

    def testExtractManyPropertiesFromManyTrees(self):
        file = open(name=MANY_TREES)
        parsedData = TreeData.parse(file)
        for i in range(0, len(parsedData)):
            assert('onStreet' in parsedData[i])
            assert('onStreetBlock' in parsedData[i])
            assert('civicNumber' in parsedData[i])
            assert('address' in parsedData[i])
            assert('commonName' in parsedData[i])
            assert('neighbourhoodName' in parsedData[i])
            assert('cell' in parsedData[i])
            assert('heightRangeID' in parsedData[i])
        file.close()

    def testNonPropertyError(self):
        file = open(name=MISSING)
        error_message = "'NoneType' object has no attribute 'text'"
        self.assertRaisesMessage(AttributeError, error_message, TreeData.parse, file)
        file.close()