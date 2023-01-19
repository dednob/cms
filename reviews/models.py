from django.db import models
import uuid


# Create your models here.
def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "cmsprojects_%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class Review(models.Model):
    reviewer_name = models.CharField(max_length=500, null=True)
    designation = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to=generate_filename, null=True)
    review = models.TextField(null=True)
