import datetime
from django.db import models
import uuid
from projects.models import Projects


# Create your models here.
def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "cmsprojects_%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class Campaigns(models.Model):
    title = models.CharField(max_length=500)
    details = models.TextField()
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    image = models.ImageField(upload_to=generate_filename, null=True)
    date = models.DateTimeField( auto_now_add=True, blank=True)
    projects = models.ManyToManyField(Projects, related_name="campaigns")
