from django.db import models
from django.conf import settings


# Create your models here.
class App(models.Model):
    app_name = models.CharField(max_length=256)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.app_name


class Post(models.Model):
    anything = models.CharField(max_length=256)

    def __str__(self):
        return self.anything
# Create your models here.
