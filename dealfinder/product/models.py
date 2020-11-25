from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify 
# Create your models here.

class Product(models.Model):

    CONDITION_TYPE = (
        ("New" , "New"),
        ("Used" , "Used")
    )
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    mobile = models.CharField(max_length=12)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    condition = models.TextField(max_length=50, choices=CONDITION_TYPE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='main_product/',blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)        

    def __str__(self):
        return self.name  


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/',blank=True, null=True)

    class Meta :
        verbose_name = 'productimage'
        verbose_name_plural = 'product Images'

    def __str__(self):
        return self.product.name


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/',blank=True, null=True)
    
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)  

    class Meta :
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name      


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    
    class Meta :
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand_name  