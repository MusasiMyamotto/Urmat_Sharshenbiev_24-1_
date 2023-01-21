from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)



