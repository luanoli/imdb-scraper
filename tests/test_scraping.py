import unittest
import jsonlines
import os.path
from scraper import scraper


class CheckScraping(unittest.TestCase):

    def test_scraping_by_genre(self):
        titles = scraper.do_scraping_by_genre('comedy')
        self.assertEqual(len(titles), 500)

    def test_jsonl_output(self):
        scraper.jsonl_output(
            'horror', ["horror1", "horror2", "horror3", "horror4"])
        with jsonlines.open('output/horror.jsonl') as reader:
            for obj in reader:
                self.assertEqual(len(obj), 4)

    def test_number_of_titles(self):
        genre = 'comedy'

        if os.path.isfile('output/' + genre + '.jsonl'):
            with jsonlines.open('output/' + genre + '.jsonl') as reader:
                for obj in reader:
                    self.assertEqual(len(obj), 500)


if __name__ == '__main__':
    unittest.main()
