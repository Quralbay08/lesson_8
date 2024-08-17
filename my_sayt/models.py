from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=225,verbose_name='categorya ati:')
    slug=models.SlugField(verbose_name='Slug category:',max_length=225)
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categorys'
    
    def __str__(self):
        return self.category_name


class Blogs(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    title=models.CharField(max_length=255,verbose_name='ati:')
    text=models.TextField(verbose_name='text:')
    image1=models.ImageField(verbose_name='1 photo(shart emes):',
                             blank=True,null=True)
    image2=models.ImageField(verbose_name='2 photo(shart emes):',
                             blank=True,null=True)
    image3=models.ImageField(verbose_name='3 photo(shart emes):',
                             blank=True,null=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Blog'
        verbose_name_plural='Blogs'
    
    def __str__(self):
        return self.title
    