from django.db import models
import uuid


def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "cms-donate_%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class Donate(models.Model):
    title = models.CharField(max_length=10000)
    details = models.TextField(null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    image = models.ImageField(upload_to=generate_filename, null=True)
