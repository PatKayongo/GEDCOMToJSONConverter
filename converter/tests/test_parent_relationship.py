from django.test import TestCase
from converter.models import Person, ParentRelationship, ParentRelationshipType

class ParentRelationshipTestCase(TestCase):

	def test_parent_and_child_set_on_initialization(self):
		parent = Person("daddy")
		relationship = ParentRelationshipType.BiologicalFather
		child = Person("child")
		relationship = ParentRelationship(parent, relationship, child)

		self.assertEqual(relationship.parent, parent)
		self.assertEqual(relationship.parentRelationshipType, relationship)
		self.assertEqual(relationship.child, child)