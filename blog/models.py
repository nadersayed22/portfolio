from django.db import models

# Create your models here.
from django.utils.text import slugify


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "blog/%s.%s" % (instance.id, extension)


class post(models.Model):
    tittle = models.CharField(max_length=100)
    date_published = models.DateTimeField()
    body_text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tittle)
        super(post, self).save(*args, **kwargs)

    def __str__(self):
        return self.tittle

    def summary(self):
        return self.body_text[:250]
