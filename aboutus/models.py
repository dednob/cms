from django.db import models
import uuid


# Create your models here.
def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "cmsaboutus_%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class Aboutus(models.Model):
    title = models.CharField(max_length=500)
    details = models.TextField()
    slug = models.SlugField(max_length=255, null=True, unique=True)
    image = models.ImageField(upload_to=generate_filename, null=True)



class Team(models.Model):
    employee_name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    image = models.ImageField(upload_to=generate_filename, null=True)
    priority = models.IntegerField(default=1)
    

