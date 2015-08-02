
from django.test import TestCase
from django_fantasy import models


class FixtureTest(TestCase):
    fixtures = ['fantasy-database.json']

    def test_data(self):
        authors = models.Author.objects.values_list('name', flat=True)

        self.assertEqual(len(authors), 2)
        self.assertEqual(authors[0], 'J. R. R. Tolkien')
        self.assertEqual(authors[1], 'J. K. Rowling')
