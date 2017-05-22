#link this file to the search bar file and views_search.py I created before. 
# Pass the query into getGoogleLinks()function with the number 0.
# example:  query = Trump, getGoogleLinks("Trump", "0")


import urllib
import mechanize
from bs4 import BeautifulSoup
import re


def getGoogleLinks(link, depth):

# create the browser and change the useragent
	br = mechanize.Browser()
	br.set_handle_robots(False)	# We don't want our browser to be seen as robotic script
	br.addheaders = [('User-agent','chrome')]

# replace space with +, look up the word in google, and return 100 links
	term = link.replace(" ","+")
	query = "http://www.google.com/search?num=100&q="+term+"&start="+depth

	htmltext = br.open(query).read()

	soup = BeautifulSoup(htmltext)

	search = soup.findAll('div', attrs = {'id':'search'})

	searchtext = str(search[0])

	soup1 = BeautifulSoup(searchtext)
	list_items = soup1.findAll('li')

	regex = "q(?!.*q).*?&amp"	#splitting the text so the it would direct to the website
	pattern = re.compile(regex)

	results_array = []

	for li in list_items:
		soup2 = BeautifulSoup(str(li))
		links = soup2.findAll('a')
		source_link = links[0]
		source_url = re.findall(pattern, str(source_link))
		if len(source_url)>0:
			results_array.append(str(source_url[0].replace("q=","").replace("&amp",""))

	return results_array 


print getGoogleLinks( "Donald Trump","0") #the 0, will give you the first 100 links. if you change
										  # to 100 then it will give you the next 100 links
