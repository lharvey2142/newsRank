import redis
import requests
from readability.readability import Document

r = redis.StrictRedis()

def urls():
    for url in open('urls.txt', 'r'):
        if not r.hexists('url-content', url):
            yield url

if __name__ == '__main__':
    for url in urls():
        try:
            response = requests.get(url, timeout=10)
            
        # Only store the content if the page load was successful
            if response.ok:
                page_content = Document(response.content).summary()
                r.hset('url-content', url, page_content)
        except:
            print( 'Error processing URL: %s' % url)
            
    print( 'Processed all URLs')
