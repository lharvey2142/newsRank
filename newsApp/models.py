from django.db import models
# Create your models here.
class Article(models.Model):
    address = models.CharField(null=True,max_length = 140,default='')
    title = models.CharField(null=True,max_length = 140,default='')
    body = models.TextField(null=True)
    date = models.DateTimeField(null=True)
    result = models.CharField(null=True,max_length = 140)
    #polarity = models.IntegerField(default=0)
    positive = models.FloatField(null=True, blank=True)
    negative = models.FloatField(null=True, blank=True)
    neutral = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.title
