from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=1000)
    typo = models.CharField(max_length=30)
    slug = models.SlugField(blank=True,null=True)
    body = models.TextField(max_length=50000)
    thumnail = models.ImageField(default='',blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE,)

    def save(self,*args,**kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title[0:50]+'-'+ (self.typo))
        super(Article,self).save(*args,**kwargs)


    def __str__(self):
        return self.title

    def info(self):
        return self.body[0:100]

    def time(self):
        if (len(self.body) >100):
            return '4 Mins'
        else:
            return '2 Mins'