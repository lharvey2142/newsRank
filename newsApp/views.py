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
import nltk

def getAddress(a):
    import urllib.parse
    parsed_uri = urllib.parse.urlparse(a.address)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    #domain = a.address

    print(domain)
    return domain #print domain
# gives
def newsfeatures(a):
    features = {}
    features['url'] = getAddress(a)#a.address
    print('url cleaned')
    print(features['url'])
    features['address'] = a.address
    #features['title'] = a.title
    #features['body'] = a.body
    #features['length'] = len(a.body)
    #features['real'] = True if a.address in knownFakeSites else False
    #features['date'] = a.date
    return features

def extract(request):
    print(request.GET.get('url_to_clean'))
    
	#from newspaper import Article
    a = newspaper.Article(request.GET.get('url_to_clean'))
    a.download()
    #author = a.authors#[0] if len(a.authors) > 0 els
    #address = a.url
    #title = a.title
    #body = a.text
    #date = a.publish_date

    article = Article(address = a.url,title = a.title,body = a.text,date = a.publish_date)
    

    #article.save() #uncomment when saving to database

    a.parse()
    a.nlp()
    '''
    classification logic insert here

    '''
    true_entries = Article.objects.filter(result='reliable')
    fake_entries = Article.objects.filter(result='unreliable')
    print('true entries')
    print(len(true_entries))
    print('fake entries')
    print(len(fake_entries))
    import random
    fake = [(newsfeatures(n),'unreliable') for n in fake_entries]
    true = [(newsfeatures(n),'reliable') for n in true_entries]
    random.shuffle(fake)
    random.shuffle(true)
    #true = true[:2300]
    #fake = fake[:2300]

    labeled_data = ( true + fake)
    
    random.shuffle(labeled_data)

    feature_set = [(n, res) for (n, res) in labeled_data]
    train_set = feature_set[:4000]
    test_set = feature_set[4000:]

    classifier = nltk.NaiveBayesClassifier.train(train_set)

    message = article.address + " is probably " + classifier.classify(newsfeatures(article)) + ". (accuracy : " + str(round(nltk.classify.accuracy(classifier, test_set) * 100, 2)) + "%)"
    print(message)
    #end classification logic
    return render(request, 'newsApp/extract.html', {'message':message,'result':'reliable/unreliable','url':a.url, 'title': a.title,'authors':a.authors,'text': a.text,'publish_date': a.publish_date,'keywords':a.keywords,'summary':a.summary,'videos':a.movies,'html':a.html,'top_image':a.top_image})
