from django.db import models

# Create your models here.
class Products(models.Model):
    Name = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)
    Desc = models.TextField()
    Price = models.IntegerField()
    Image = models.ImageField(upload_to='pics')
class Cart(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.CharField(max_length=20)
    prod_id=models.IntegerField()
