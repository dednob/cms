from django.db import models

# Create your models here.

class Aboutus(models.Model):
    title = models.CharField(max_length=500)
    details = models.TextField()
    # blog_image = models.ImageField(upload_to=generate_filename, null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True)

