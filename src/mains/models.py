from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'category' 
        verbose_name_plural = 'categories' 
        
        
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='' , null=True , blank=True)
    image = models.ImageField(upload_to='products/')
    
    @staticmethod
    def products_by_cat_id(category_id):
        if category_id: 
            return Product.objects.filter(category = category_id)
        else:
            return Product.objects.all();