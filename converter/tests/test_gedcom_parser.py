from django.test import TestCase
from converter.business_logic.gedcom_parser import GedcomParser
from converter.business_logic.exceptions.invalid_file_exception import InvalidFileException
from converter.models import Person, ParentRelationship, ParentRelationshipType

class GedcomParserTestCase(TestCase):

	def setUp(self):
		self.parser = GedcomParser()

	def test_fileContentHasNoHead_exceptionThrown(self):
		
		fileContent = "1 INDI"

		with self.assertRaises(InvalidFileException) as contextManager:
			self.parser.parseGedcomContent(fileContent)

		exception = contextManager.exception
		self.assertEqual(str(exception), "The file has no HEAD")

	def test_fileHasPerson_PersonCreated(self):
		fileContent = "0 HEAD"
		fileContent = fileContent + " \n 0 @I1@ INDI"
		fileContent = fileContent + " \n 1 NAME Patrick"
		fileContent = fileContent + " \n 0 TRLR"
		
		people = self.parser.parseGedcomContent(fileContent)

		self.assertIsNotNone(people)
		self.assertEqual(people[0].name, "Patrick")


