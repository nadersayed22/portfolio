from django.db import models


# Create your models here.


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "blog/%s.%s" % (instance.id, extension)


class post(models.Model):
    tittle = models.CharField(max_length=100)
    date_published = models.DateTimeField()
    body_text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.tittle

    def summary(self):
        return self.body_text[:250]
