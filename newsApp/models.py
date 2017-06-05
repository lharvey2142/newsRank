from django.db import models
from django.forms import ModelForm #needed to use ModelForm
# Create your models here.


'''
Article model
stores information retrieved from web scraper
'''
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
'''
# code to create Forms and search model
class Search(models.Model):
    address = models.CharField(null=True,max_length = 140,default='')
    #title = models.CharField(null=True,max_length = 140,default='')

    def __str__(self):
        return self.title

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['address', 'title', 'body',]

class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = ['address', ]

'''