from django.shortcuts import render
# Create your views here.
from django.core.urlresolvers import reverse
import sys

sys.path.append('/Users/froyvalencia/newsRank')
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
import django
django.setup()

from django.contrib.auth.models import User
users = User.objects.all()
from newsApp.models import Article
import newspaper
import nltk

#imports for search 
import urllib.parse 
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import re

def getAddress(a):
    import urllib.parse
    parsed_uri = urllib.parse.urlparse(a.address)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain

def newsfeatures(a):
    features = {}
    features['url'] = getAddress(a)
    #print('url cleaned')
    #print(features['url'])
    #features['address'] = a.address
    #features['title'] = a.title
    #features['body'] = a.body
    #features['length'] = len(a.body)
    return features
'''
def deleteExtras():
    print("starting delete")
    Article.objects.filter(result='').delete()
    print('end delete')
    from django.db.models import Count
    print("starting delete doubles")

    for a in Article.objects.values_list('address', flat=True).distinct():
        Article.objects.filter(pk__in=Article.objects.filter(address=a).values_list('id', flat=True)[1:]).delete()
    print('end delete doubles')

    #duplicates = Article.objects.values('address').annotate(address_count=Count('address')).filter(address_count__gt=1)
    #for data in duplicates:
    #    address = data['address']
    #    Article.objects.filter(address=address).order_by('address')[1:].delete()
'''
def extract(request):
    #deleteExtras()
    print(request.GET.get('url_to_clean'))
    a = newspaper.Article(request.GET.get('url_to_clean'))
    a.download()
    current = Article.objects.filter(address=request.GET.get('url_to_clean'))    
    article = Article(
        address = a.url,
        title = a.title,
        body = a.text,
        date = a.publish_date,
        )
    #article.save() #uncomment when saving to database
    a.parse()
    a.nlp()
    if len(current) > 0:
        return render(
        request,
        'newsApp/extract.html',
        {
            'accuracy':"Retrieved from database assumed 100%",
            'result':current[0].result,
            'url':a.url, 
            'title': a.title,
            'authors':a.authors,
            'text': a.text,
            'publish_date': a.publish_date,
            'keywords':a.keywords,
            'summary':a.summary,
            'videos':a.movies,
            'html':a.html,
            'top_image':a.top_image
        },
        )

    #classification logic 
    true_entries = Article.objects.filter(result='reliable')
    fake_entries = Article.objects.filter(result='unreliable')
    #print('true entries')print(len(true_entries))
    #print('fake entries')print(len(fake_entries))
    

    import random
    fake = [(newsfeatures(n),'unreliable') for n in fake_entries]
    true = [(newsfeatures(n),'reliable') for n in true_entries]
    random.shuffle(fake)
    random.shuffle(true)
    labeled_data = (true + fake)
    random.shuffle(labeled_data)

    feature_set = [(n, res) for (n, res) in labeled_data]
    train_set = feature_set[:5500]
    test_set = feature_set[5500:]

    classifier = nltk.NaiveBayesClassifier.train(train_set)
    result = classifier.classify(newsfeatures(article))
    accuracy = str(round(nltk.classify.accuracy(classifier, test_set) * 100, 2)) + "%"
    #message = article.address + " is probably " + result + ". (accuracy : " + str(round(nltk.classify.accuracy(classifier, test_set) * 100, 2)) + "%)"
    #end classification logic
    return render(
        request,
        'newsApp/extract.html',
        {
            'accuracy':accuracy,
            'result':result,
            'url':a.url, 
            'title': a.title,
            'authors':a.authors,
            'text': a.text,
            'publish_date': a.publish_date,
            'keywords':a.keywords,
            'summary':a.summary,
            'videos':a.movies,
            'html':a.html,
            'top_image':a.top_image
        },
    )

def search(request):
    print(request.GET.get('q'))
    link = request.GET.get('q')
    # create the browser and change the useragent
    br = RoboBrowser()
    # replace space with +, look up the word in google, and return 100 links
    term = link.replace(" ","+")
    query = "https://www.google.com/search?q="+term

    br.open(query)
    htmltext = str(br.parsed)

    soup = BeautifulSoup(htmltext, "lxml")

    search = soup.findAll('div', attrs = {'id':'search'})

    searchtext = str(search[0])

    soup1 = BeautifulSoup(searchtext)
    list_items = soup1.findAll('li')

    #splitting the text so the it would direct to the website
    regex = "q(?!.*q).*?&amp"   
    pattern = re.compile(regex)
    results_array = []
    print(list_items)
    for li in list_items:
        soup2 = BeautifulSoup(str(li))
        links = soup2.findAll('a')
        source_link = links[0]
        source_url = re.findall(pattern, str(source_link))
        if len(source_url)>0:
            print('loop')
            results_array.append(str(source_url[0].replace("q=","").replace("&amp","")))
    final = []
    for n in results_array:
        print(n)
        if n.find('http') != -1: 
            final.append(n[n.find('http'):])    
        elif n.find('www.') != -1:
            final.append('http://'+n[n.find('www.'):])

    for link in final:
        print(link)
        
    return render(request, 'newsApp/links.html', {'links': final,'query':link})

