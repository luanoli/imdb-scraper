import sys
import os.path
import unittest

import jsonlines

sys.path.append(".")

from scraper import scraper


class CheckScraping(unittest.TestCase):

    def test_scraping_by_genre(self):
        titles = scraper.do_scraping_by_genre('comedy')
        self.assertEqual(len(titles), 500)

    def test_jsonl_output(self):
        scraper.jsonl_output(
            'horror', [
                {"title": "horror1"},
                {"title": "horror2"},
                {"title": "horror3"},
                {"title": "horror4"}
            ])

        with jsonlines.open('output/horror.jsonl') as reader:
            number_of_lines = 0

            for obj in reader:
                number_of_lines += 1

            os.remove('output/horror.jsonl')
            self.assertEqual(number_of_lines, 4)

    def test_number_of_titles(self):
        genre = 'comedy'

        if os.path.isfile('output/' + genre + '.jsonl'):
            with jsonlines.open('output/' + genre + '.jsonl') as reader:

                number_of_lines = 0

                for obj in reader:
                    number_of_lines += 1

                self.assertEqual(number_of_lines, 500)


if __name__ == '__main__':
    unittest.main()
