from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    typo = models.CharField(max_length=30)
    slug = models.SlugField()
    body = models.TextField()
    thumnail = models.ImageField(default='',blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    def info(self):
        return self.body[0:100]

    def time(self):
        if (len(self.body) >100):
            return '4 Mins'
        else:
            return '2 Mins'