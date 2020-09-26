from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.name) + ' ' + self.text[:50]
