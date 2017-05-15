from django.conf.urls import url
from django.views.generic import ListView, DetailView
from newsApp.models import Article
from . import views

urlpatterns = [ 
    #url(r'^$', 'hello fill in later',template_name="newsApp/newsApp.html")),
    url(r'^$', ListView.as_view(queryset=Article.objects.all().order_by("-date")[:25],template_name="newsApp/newsApp.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Article,template_name="newsApp/article.html")),
    ]