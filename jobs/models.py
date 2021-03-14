from django.db import models

# Create your models here..
def upload_image(instance,filename):
    name , ext = filename.splite(".")
    return  "job/%s.%s"%(instance.id,ext)
class Job(models.Model):
    image=models.ImageField(upload_to=upload_image)
    summary=models.CharField(max_length=200)