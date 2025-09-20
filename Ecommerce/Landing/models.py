from django.db import models

class Items_1(models.Model):
    product = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='items_1/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product
    
class Items_2(models.Model):
    product = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='items_2/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product