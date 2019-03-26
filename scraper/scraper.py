import requests
import jsonlines
import sys
from bs4 import BeautifulSoup

_GENRES = ['comedy', 'sci-fi', 'horror', 'romance', 'action',
           'thriller', 'drama', 'mystery', 'crime', 'animation',
           'adventure', 'fantasy', 'comedy,romance', 'action,comedy']


def do_request(url):
    print(url)

    response = requests.get(url)

    if response.status_code != 200:
        sys.exit('Page not found')

    return BeautifulSoup(response.content, 'html.parser')

    #contents = soup.select('lister-item-content')


def parser(soup):
    links = soup.select('h3.lister-item-header a:nth-of-type(1)')

    titles = [link.get_text() for link in links]

    return titles


def do_scraping():
    for genre in _GENRES:

        print('\n')
        print(genre)

        titles = do_scraping_by_genre(genre)

        jsonl_output(genre, titles)


def do_scraping_by_genre(genre):
    page = 1
    titles = []

    while page < 500:

        url = build_url(genre, page)

        soup = do_request(url)

        new_titles = parser(soup)

        titles = titles + new_titles

        page += 50

    return titles


def jsonl_output(genre, titles):
    with jsonlines.open('output/' + genre + '.jsonl', mode='w') as writer:
        writer.write(titles)


def build_url(genre, page):
    return "https://www.imdb.com/search/title?genres=" + genre + \
        "&sort=user_rating,desc&start=" + str(page)
