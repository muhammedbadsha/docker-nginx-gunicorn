from django.db import models

# Create your models here.

class Notes(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    images = models.ImageField(upload_to='images',blank=True,null=True)
    title = models.CharField(max_length=300,null=True,blank=True)
    body = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self) -> str:
        return self.title