from enum import Enum
from django.db import models

# Create your models here.

class Person:
	name = None
	dateOfBirth = None
	sourceID = None
	isFemale = None
	parentRelationships = []
	marriages = []
	def __init__(self, name):
		self.name = name

class MarriageStatus(Enum):
	Married = 1
	Divorced = 2

class Marriage:
	marriageDate = None

	def __init__(self, husband, wife):
		self.husband = husband
		self.wife = wife

class ParentRelationshipType(Enum):
	BiologicalMother = 1
	BiologicalFather = 2
	AdoptedMother = 3
	AdoptedFather = 4

class ParentRelationship:
	def __init__(self, parent, relationshipType, child):
		self.parent = parent
		self.parentRelationshipType = relationshipType
		self.child = child