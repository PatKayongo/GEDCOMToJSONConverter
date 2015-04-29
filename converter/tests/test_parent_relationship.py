from django.test import TestCase
from converter.models import Person, ParentRelationship, ParentRelationshipType

class ParentRelationshipTestCase(TestCase):

	def test_parent_and_child_set_on_initialization(self):
		parent = Person("daddy")
		relationshipType = ParentRelationshipType.BiologicalFather
		child = Person("child")
		relationship = ParentRelationship(parent, relationshipType, child)

		self.assertEqual(relationship.parent, parent)
		self.assertEqual(relationship.parentRelationshipType, relationshipType)
		self.assertEqual(relationship.child, child)