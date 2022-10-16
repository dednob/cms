import datetime
from django.db import models
import uuid
# from areaofwork.models import Areaofwork


# Create your models here.
def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "cmsprojects_%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class Gallery(models.Model):
    title = models.CharField(max_length=500)
    details = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=500, null=True, unique=True)
    image = models.ImageField(upload_to=generate_filename, null=True)
    
    
