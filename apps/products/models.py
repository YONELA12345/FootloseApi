from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    created_date=models.DateTimeField(auto_now_add=True)

    created_by=models.CharField(
        default='',
        max_length=250,
        null=True
    )

    deleted=models.BooleanField(
        null=True,
        default=False
    )

class Color(models.Model):
    name = models.CharField(max_length=50)
    
    created_date=models.DateTimeField(auto_now_add=True)

    created_by=models.CharField(
        default='',
        max_length=250,
        null=True
    )

    deleted=models.BooleanField(
        null=True,
        default=False
    )



class ModelP(models.Model):
    name = models.CharField(max_length=100)

    created_date=models.DateTimeField(auto_now_add=True)

    created_by=models.CharField(
        default='',
        max_length=250,
        null=True
    )

    deleted=models.BooleanField(
        null=True,
        default=False
    )


class Size(models.Model):
    name = models.CharField(max_length=50)

    created_date=models.DateTimeField(auto_now_add=True)

    created_by=models.CharField(
        default='',
        max_length=250,
        null=True
    )

    deleted=models.BooleanField(
        null=True,
        default=False
    )



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    modelp = models.ForeignKey(ModelP, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)

    created_by=models.CharField(
        default='',
        max_length=250,
        null=True
    )

    deleted=models.BooleanField(
        null=True,
        default=False
    )


