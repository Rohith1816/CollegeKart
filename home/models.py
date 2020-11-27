from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField(max_length=400)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.username:
            self.slug = slugify(self.username)
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.username)