import timeit
import newspaper
from newspaper import Article


def get_headlines():


    URLs = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.derspiegel.de/',
        'http://www.bbc.co.uk/',
        'https://theguardian.com',]


for url in URLs:
    result = newspaper.build(url, memoize_articles=False)
    print('\n''The headlines from %s are' % url, '\n')
for i in range(1, 6):
    art = result.articles[i]
    art.download()
    art.parse()
    print(art.title)


if name == '__main__':
    elapsed_time = timeit.timeit(
    "get_headlines()", setup="from main import get_headlines", number=2)/2
    print(elapsed_time)
