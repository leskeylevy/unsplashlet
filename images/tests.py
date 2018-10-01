from django.test import TestCase
from .models import Location, Image, Category


# Create your tests here.
class LocationTest(TestCase):
    def setUp(self):
        self.test_location = Location(location='githu')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_location,Location))

    def test_data(self):
        self.assertTrue(self.test_location.location,"githu")

    def test_save(self):
        self.test_location.save()
        location = Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_delete(self):
        location = Location.objects.filter(id=1)
        location.delete()
        test = Location.objects.all()
        self.assertTrue(len(test) == 0)

    def test_update(self):
        self.test_location.save()
        self.update_locations = Location.objects.filter(location='githu').update(location ='Kiabuu')
        self.updated_locations = Location.objects.get(location='Kiabuu')
        self.assertTrue(self.updated_locations.location,'Kiabuu')


class CategoryTest(TestCase):
    def setUp(self):
        self.test_category = Category(category='test')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_category,Category))

    def test_data(self):
        self.assertTrue(self.test_category.category, "test")

    def test_save(self):
        self.test_category.save()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete(self):
        category = Category.objects.filter(id=1)
        category.delete()
        cat = Category.objects.all()
        self.assertTrue(len(cat) == 0)

    def test_update_category(self):
        self.test_category.save()
        self.update_cat = Category.objects.filter(category='test').update(category='aaabbbc')
        self.updated_cat = Category.objects.get(category='aaabbbc')
        self.assertTrue(self.updated_cat.category, 'aaabbbc')

    def test_get_category_by_id(self):
        self.test_category.save()
        cat = Category.objects.get(id=1)
        self.assertTrue(cat.category, 'test')


class imageTest(TestCase):
    def setUp(self):
        self.test_location = Location(location='githu')
        self.test_location.save()
        self.test_image = Image(image_name="slim", image_description="kolumn", location=self.test_location)

    def test_instance(self):
        self.assertTrue(isinstance(self.test_image,Image))

    def test_data(self):
        self.assertTrue(self.test_image.image_name,'slim')
        self.assertTrue(self.test_image.image_description,'kolumn')

    def test_save(self):
        self.test_image.save()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete(self):
        image = Image.objects.filter(id=1)
        image.delete()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)