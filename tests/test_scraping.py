import unittest
from scraper import scraper


class CheckScraping(unittest.TestCase):

    def test_scraping(self):
        titles = scraper.do_scraping_by_genre('comedy')
        self.assertEqual(len(titles), 500)


if __name__ == '__main__':
    unittest.main()
