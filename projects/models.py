import datetime
from django.db import models
import uuid
from areaofwork.models import Areaofwork


# Create your models here.
def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "cmsprojects_%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class Projects(models.Model):
    title = models.CharField(max_length=500)
    details = models.TextField()
    slug = models.SlugField(max_length=255, null=True, unique=True)
    image = models.ImageField(upload_to=generate_filename, null=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    areaofwork = models.ManyToManyField(Areaofwork, related_name='projects')
    featured = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title
