import sys
import os.path
import unittest
import shutil

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

        if not os.path.isdir('output_test'):
            os.mkdir('output_test')

            with jsonlines.open('output_test/horror.jsonl') as reader:
                number_of_lines = 0

                for obj in reader:
                    number_of_lines += 1

                self.assertEqual(number_of_lines, 4)

    def test_number_of_titles(self):
        genre = 'comedy'

        if os.path.isfile('output/' + genre + '.jsonl'):
            with jsonlines.open('output/' + genre + '.jsonl') as reader:

                number_of_lines = 0

                for obj in reader:
                    number_of_lines += 1

                self.assertEqual(number_of_lines, 500)

    def tearDown(self):
        if os.path.isdir('output_test'):
            shutil.rmtree('output_test')


if __name__ == '__main__':
    unittest.main()
