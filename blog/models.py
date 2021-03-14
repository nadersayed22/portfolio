from django.db import models


# Create your models here.


def image_upload(self, filename):
    imagename,exttantion = filename.split(".")
    return "media/%S.%S"%(self.id, exttantion)

class post(models.Model):
    tittle = models.CharField(max_length=100)
    date_published = models.DateTimeField()
    body_text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.tittle

    def summry(self):
        return self.body_text[:250]
