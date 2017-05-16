urls = [line.split('",')[0][1:] for line in open('../fakes')]
for url in urls:
    print(url)
