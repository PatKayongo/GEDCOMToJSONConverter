from django.test import TestCase
from converter.models import Person

class PersonTestCase(TestCase):
	def setUp(self):
		self.name = "name"

	def test_name_set_on_initialization(self):
		"""Test name is set on initialization"""
		person = Person("Thando")
		self.assertEqual(person.name, "Thando")