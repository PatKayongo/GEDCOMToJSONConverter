from django.test import TestCase

# Create your tests here.
from converter.models import Person, Marriage

class MarriageTestCase(TestCase):

	def test_husband_and_wife_set_on_initialization(self):
		"""Test husband and wife are set on initialization"""
		husband = Person("Michael")
		wife = Person("Mary")
		marriage = Marriage(husband, wife)

		self.assertEqual(marriage.husband, husband)
		self.assertEqual(marriage.wife, wife)