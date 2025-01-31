from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BookModel(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    author=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to="images")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    