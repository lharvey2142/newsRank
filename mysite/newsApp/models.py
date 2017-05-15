from django.db import models

# Create your models here.
class Article(models.Model):
    address = models.CharField(max_length = 140,default='')
    title = models.CharField(max_length = 140,default='')
    body = models.TextField()
    date = models.DateTimeField()
    result = models.CharField(max_length = 140)
    polarity = models.IntegerField(default=0)
    def __str__(self):
        return self.title