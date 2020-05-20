from django.db import models

# Create your models here.
class sayariinfo(models.Model):
    id = models.AutoField
    uploadImg = models.ImageField(upload_to="store/sayariimages", default="")
    description = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    pub_date = models.DateField()
    category = models.CharField(max_length=200, default="")