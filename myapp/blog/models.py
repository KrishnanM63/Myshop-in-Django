from django.db import models


class registerform(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    confir_password =models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="products/")
    
    def __str__(self):
        return self.name
    
    
    
