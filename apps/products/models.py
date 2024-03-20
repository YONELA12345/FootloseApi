from sysconfig import get_path
from django.db import models
from utils.manage_media import get_path, manage_image
from utils.constants.media import IMAGE


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
    price = models.FloatField(
        blank = True,
        null = True,
        default=0)
    image = models.ImageField(
        upload_to=get_path(IMAGE, "PRODUCT"), 
        null=True, 
        blank=True
    )
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

    def save(self, *args, **kwargs):
        if self.image:
            self.image=manage_image(self.image, "PHOTO_")

        super(Product, self).save(*args, **kwargs)
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return None


