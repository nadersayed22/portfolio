from django.db import models


# Create your models here..
def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "blog/%s.%s" % (instance.id, extension)


class Job(models.Model):
    image = models.ImageField(upload_to=image_upload)
    summary = models.CharField(max_length=200)
