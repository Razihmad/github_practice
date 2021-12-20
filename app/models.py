from django.db import models

# Create your models here.
class FileModel(models.Model):
    file = models.FileField(verbose_name='files')



