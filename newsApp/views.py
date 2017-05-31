from django.shortcuts import render
# Create your views here.

from django.core.urlresolvers import reverse

import sys
sys.path.append('/Users/froyvalencia/Desktop/newsRank')
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
import django
django.setup()

from django.contrib.auth.models import User
users = User.objects.all()
from newsApp.models import Article
import newspaper

def newsfeatures(a):
    features = {}
    features['url'] = a.address
    features['title'] = a.title
    features['body'] = a.text
    features['date'] = a.publish_date

def extract(request):
    print(request.GET.get('url_to_clean'))
    
	#from newspaper import Article
    a = newspaper.Article(request.GET.get('url_to_clean'))
    a.download()
    a.parse()
    a.nlp()
    #author = a.authors#[0] if len(a.authors) > 0 els
    address = a.url
    title = a.title
    body = a.text
    date = a.publish_date

    article = Article(address = a.url,title = a.title,body = a.text,date = a.publish_date)
    article.save()



    '''
    classification logic insert here
    
    '''

    return render(request, 'newsApp/extract.html', {'result':'reliable/unreliable','url':u, 'title': a.title,'authors':a.authors,'text': a.text,'publish_date': a.publish_date,'keywords':a.keywords,'summary':a.summary,'videos':a.movies,'html':a.html,'top_image':a.top_image})
