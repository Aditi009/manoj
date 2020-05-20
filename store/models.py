from django.db import models


# Create your models here.
class imageinfo(models.Model):
      id=models.AutoField
      uploadImg = models.ImageField(upload_to="store/images", default="")
      description=models.CharField(max_length=300)
      name=models.CharField(max_length=300)
      pub_date = models.DateField()
      price = models.IntegerField(default=0)
      category=models.CharField(max_length=200,default="")



