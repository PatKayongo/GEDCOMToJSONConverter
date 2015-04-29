from converter.business_logic.exceptions.invalid_file_exception import InvalidFileException
from converter.models import Person, ParentRelationship, ParentRelationshipType

class BaseElementParser:

	def parseElement(self, person):
		return None

class PersonParser(BaseElementParser):

	def parseElement(self, fileLines, person):

class GedcomParser:

	def __init__(self):
		

	def parseGedcomContent(self, fileContent):
		fileContent = fileContent.strip()
		fileLines = fileContent.splitlines()

		if (len(fileLines) == 0) or (fileLines[0].strip() != "0 HEAD"):
			raise InvalidFileException("The file has no HEAD")

		fileLines.pop(0)

		counter = 0
		while len(fileLines) > 0:
			if (fileLines[0].startswith("0")):


		person = Person()

		return person



