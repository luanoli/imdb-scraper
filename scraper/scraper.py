import requests
import jsonlines
import sys
import os.path
from bs4 import BeautifulSoup

_GENRES = ['comedy', 'sci-fi', 'horror', 'romance', 'action',
           'thriller', 'drama', 'mystery', 'crime', 'animation',
           'adventure', 'fantasy', 'comedy,romance', 'action,comedy']


def do_request(url):
    response = requests.get(url)

    if response.status_code != 200:
        sys.exit('Page not found')

    return BeautifulSoup(response.content, 'html.parser')


def parser(soup):
    itens_header = soup.select('h3.lister-item-header')

    titles = []

    for item in itens_header:
        links = item.select('a')
        title_list = [link.get_text() for link in links]
        title = " ".join(title_list).strip()
        titles.append(title)

    return titles


def do_scraping():
    for genre in _GENRES:
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
    if not os.path.isdir('output'):
        os.mkdir('output')

    with jsonlines.open('output/' + genre + '.jsonl', mode='w') as writer:
        writer.write(titles)


def build_url(genre, page):
    return "https://www.imdb.com/search/title?genres=" + genre + \
        "&sort=user_rating,desc&start=" + str(page)
