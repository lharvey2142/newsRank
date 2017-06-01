urls = [ ('\'http://www.' + line.split('",')[0][1:] + '\',') for line in open('FakeNewsSites.csv')]
for url in urls:
    print(url)
