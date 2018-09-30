from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Location(models.Model):
    location = models.CharField(max_length=30)


    def  save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,location,update):
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