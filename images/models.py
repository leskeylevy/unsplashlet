from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id, update):
        update_category = cls.objects.filter(id=id).update(category=update)
        return update_category

    def __str__(self):
        return self.category


class Location(models.Model):
    location = models.CharField(max_length=30)

    def  save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,update):
        location_update = cls.objects.filter(id=id).update(location=update)
        return location_update

    def __str__(self):
        return self.location


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pub_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,update):
        update_image=cls.objects.filter(id=id).update(target=update)
        return update_image

    @classmethod
    def get_all(cls):
        images = cls.objects.order_by('pub-date')
        return images

    @classmethod
    def get_image(cls,id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images