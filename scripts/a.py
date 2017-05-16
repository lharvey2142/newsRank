import newspaper
#from newspaper import Article
import nltk
#nltk.download('all')
knownFakeSites = ['http://www.16WMPO.com', 'http://www.24wpn.com', 'http://www.ABCNews.com.co', 'http://www.actualidadpanamericana.com', 'http://www.AmericanPoliticNews.co', 'http://www.AmericanPresident.co', 'http://www.AMPosts.com', 'http://www.ANews24.org/', 'http://www.AngryPatriotMovement.com', 'http://www.Anonjekloy.tk', 'http://www.AssociatedMediaCoverage.com', 'http://www.Aurora-News.us', 'http://www.BB4SP.com', 'http://www.BeforeItsNews.com', 'http://www.BlackInsuranceNews.com', 'http://www.BostonTribune.com', 'http://www.BuzzFeedUSA.com', 'http://www.CannaSOS.com', 'http://www.Channel18News.com', 'http://www.ChristianTimesNewspaper.com', 'http://www.ChristianToday.info', 'http://www.CivicTribune.com', 'http://www.CivicTribune.com', 'http://www.ClashDaily.com', 'http://www.CNNews3.com', 'http://www.Coed.com', 'http://www.ConservativeDailyPost.com', 'http://www.ConservativeFlashNews.com', 'http://www.ConservativeSpirit.com', 'http://www.DailyInfoBox.com', 'http://www.DailyNews10.com', 'http://www.DailyNews5.com', 'http://www.DailyNewsPosts.info', 'http://www.DailySnark.com', 'http://www.DailySurge.com', 'http://www.DailyUSAUpdate.com', 'http://www.DamnLeaks.com', 'http://www.DepartedMedia.com', 'http://www.Disclose.tv', 'http://www.DIYHours.net', 'http://www.DonaldTrumpPOTUS45.com', 'http://www.EmpireHerald.com', 'http://www.EmpireNews.net', 'http://www.EmpireSports.co', 'http://www.En-Volve.com', 'http://www.ENHLive.com', 'http://www.FedsAlert.com', 'http://www.FlashNewsCorner.com', 'http://www.FreedomDaily.com', 'http://www.FreeWoodPost.com', 'http://www.FreshDailyReport.com', 'http://www.GiveMeLiberty01.com', 'http://www.GlobalPoliticsNow.com', 'http://www.GummyPost.com', 'http://www.HealthyCareAndBeauty.com', 'http://www.HealthyWorldHouse.com', 'http://www.InterestingDailyNews.com', 'http://www.JewsNews.co.il', 'http://www.KMT11.com', 'http://www.Konkonsagh.biz', 'http://www.KY12News.com', 'http://www.LadyLibertysNews.com', 'http://www.LastDeplorables.com', 'http://www.LearnProgress.org', 'http://www.LiberalPlug.com', 'http://www.LibertyAlliance.com', 'http://www.Local31News.com', 'http://www.MadWorldNews.com', 'http://www.MajorThoughts.com', 'http://www.Mentor2day.com', 'http://www.MetropolitanWorlds.com', 'http://www.NationalReport.net', 'http://www.NBC.com.co', 'http://www.NeonNettle.com', 'http://www.Nephef.com', 'http://www.NewPoliticsToday.com', 'http://www.News4KTLA.com', 'http://www.NewsBreaksHere.com', 'http://www.NewsBySquad.com', 'http://www.NewsDaily12.com', 'http://www.NewsExaminer.net', 'http://www.NewsLeak.co', 'http://www.Newslo.com', 'http://www.NewzMagazine.com', 'http://www.NotAllowedTo.com', 'http://www.OccupyDemocrats.com', 'http://www.OnePoliticalPlaza.com', 'http://www.OpenMagazines.com', 'http://www.Politicalo.com', 'http://www.Politicono.com', 'http://www.Politicops.com', 'http://www.Politicot.com', 'http://www.PoliticsUSANews.com', 'http://www.President45DonaldTrump.com', 'http://www.Prntly.com', 'http://www.RedCountry.us', 'http://www.RedRockTribune.com', 'http://www.Religionlo.com', 'http://www.ReligionMind.com', 'http://www.Rogue-Nation3.com', 'http://www.RumorJournal.com', 'http://www.SatiraTribune.com', 'http://www.Smag31.com', 'http://www.SocialEverythings.com', 'http://www.Success-Street.com', 'http://www.SupremePatriot.com', 'http://www.TDTAlliance.com', 'http://www.TeaParty.org', 'http://www.ThatViralFeed.net', 'http://www.The-Insider.co', 'http://www.TheBigRiddle.com', 'http://www.TheInternetPost.net', 'http://www.TheLastLineOfDefense.org', 'http://www.TheMoralOfTheStory.us', 'http://www.TheNationalMarijuanaNews.com', 'http://www.TheNet24h.com', 'http://www.TheNewYorkEvening.com', 'http://www.ThePoliticalInsider.com', 'http://www.TheRightists.com', 'http://www.TheSeattleTribune.com', 'http://www.TheTrumpMedia.com', 'http://www.TheUSA-News.com', 'http://www.TheWashingtonPress.com', 'http://www.Times.com.mx', 'http://www.TMZWorldNews.com', 'http://www.TrueAmericans.me', 'http://www.TrueTrumpers.com', 'http://www.UndergroundNewsReport.com', 'http://www.UniversePolitics.com', 'http://www.UrbanImageMagazine.com', 'http://www.USA-Radio.com', 'http://www.USA-Television.com', 'http://www.USADailyInfo.com', 'http://www.USADailyPost.us', 'http://www.USADailyTime.com', 'http://www.USADoseNews.com', 'http://www.USAFirstInformation.com', 'http://www.USANewsToday.com', 'http://www.USAPolitics24hrs.com', 'http://www.USAPoliticsToday.com', 'http://www.USAPoliticsZone.com', 'http://www.USASnich.com', 'http://www.USATodayNews.me', 'http://www.USHealthyAdvisor.com', 'http://www.USHealthyLife.com', 'http://www.USHerald.com', 'http://www.USInfoNews.com', 'http://www.USPOLN.com', 'http://www.USPostman.com', 'http://www.ViralActions.com', 'http://www.VoxTribune.com', 'http://www.WashingtonFeed.com', 'http://www.WashingtonPost.com.co', 'http://www.WorldNewsDailyReport.com', 'http://www.WorldPoliticsNow.com']

import tweetParser
knownFakeSites = []
all = []
for url in knownFakeSites:
    fake_paper = None
    try:
        fake_paper = newspaper.build(url)
        print(url + ' contains ' + str(len(fake_paper.articles)) + ' fake articles')
        print(len(fake_paper.articles))
        #for a in fake_paper.articles:
            #all.append(a)
    except: #ValueError:
        print(url)
        print('url is bad')
        continue


    for article in fake_paper.articles:
        article.download()
        article.parse()
        print('author:**************************\n');print(article.authors)
        print('text:**************************\n');print(article.text)
        print('title:**************************\n');print(article.title)
        print('end!!!!!!!!******')
        article.nlp()
        print('keywords:**************************\n');print(article.keywords)
        print('summary:**************************\n');print(article.summary)

def parseArticle(url):
    a = newspaper.Article(url)
    a.download()
    a.parse()
    print('title')
    print(a.title)
    print('text')
    print(a.text)
    print('author')
    print(a.authors)
    a.nlp()
    print('keywords')
    print(a.keywords)
    print('summary')
    print(a.summary)


def createArticle(url):
#    from newsApp.models import Article
#    from django.contrib.auth.models import User
    
    a = newspaper.Article(url)
    a.download()
    a.parse()
    print('title')
    print(a.title)
    print('text')
    print(a.text)
    print('author')
    print(a.authors)
    a.nlp()
    print('keywords')
    print(a.keywords)
    print('summary')
    print(a.summary)
    



parseArticle('http://www.cnn.com/2017/05/15/politics/trump-russia-classified-information/index.html')
x,y,z = tweetParser.getSentiment('http://www.cnn.com/2017/05/15/politics/trump-russia-classified-information/index.html',2000)
print(x)
print(y)
print(z)

cnn_paper = newspaper.build('http://www.cnn.com')
print('size: \n'+str(cnn_paper.size()))
sites = [c for c in cnn_paper.category_urls()]
print(sites)
'''
print('start other')
for a in cnn_paper.articles:
    article.download()
    article.parse()
    print('author:\n');print(article.authors)
    print('text:\n');print(article.text)
    print('title: \n');print(article.title)
    print('end!!!!!!!!******')

    print('keywords:\n');print(article.keywords)
    print('summary:\n');print(article.summary)
'''
fox_paper = newspaper.build('http://www.foxnews.com')
fsites = [c for c in fox_paper.category_urls()]
print(fsites)

'''
print('size: \n' + str(fox_paper.size()))
for article in fox_paper.articles:
    article.download()
    article.parse()
    print('author:\n');print(article.authors)
    print('text:\n');print(article.text)
    print('title: \n');print(article.title)
    print('end!!!!!!!!******')
    article.nlp()
    print('keywords:\n');print(article.keywords)
    print('summary:\n');print(article.summary)

'''
