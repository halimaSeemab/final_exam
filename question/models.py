from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=225) 
    content = models.CharField(max_length=225)
    pub_date = models.DateField(null=True)
    athur = models.CharField(max_length=225,null=True)




class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()