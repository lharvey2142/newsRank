from django.test import TestCase
# Create your tests here.
from newsApp.models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(address="http://www.foxbusiness.com/markets/2017/07/01/sears-says-some-kmart-customer-credit-card-numbers-compromised.html")
        Article.objects.create(address="http://www.theonion.com/")

    def test_article_is_reliable(self):
        """Articles that can speak are correctly identified"""
        a1 = Article.objects.get(address="http://www.foxbusiness.com/markets/2017/07/01/sears-says-some-kmart-customer-credit-card-numbers-compromised.html")
        #
	    self.assertEqual(a1.result,'reliable')

    def test_article_is_unreliable(self):
    	a1 = Article.objects.get(address="http://www.theonion.com/")
    	#
    	self.assertEqual(a1.result,'unreliable')

