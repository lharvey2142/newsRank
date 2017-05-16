import newspaper
cnn_paper = newspaper.build('http://www.cnn.com')
#cnn_paper = newspaper.build('http://www.foxnews.com')
print(len(cnn_paper.articles))
for article in cnn_paper.articles:
    print(article.download())
    print(article.parse())
    print(article.authors)
    print(article.text)
    print(article.title)
    print('end!!!!!!!!******')
    print(article.nlp())
    print(article.keywords)
    #print(article.summary)
    
    
