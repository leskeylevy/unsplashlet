from django.test import TestCase
from .models import Location, Image, Category


# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.test_location = Location(location='githu')
