import unittest
from phonebook import Phonebook

class PhonebookTestCase(unittest.TestCase):

	def tearDown(self):
		pass
	
	
	def test_create_contact(self):
		contact = Phonebook()
		response = contact.create_contact("Arnold", "07449494")
		self.assertEqual(response["message"], "Contact created")
		pass

	def test_cannot_create_duplicate_contact(self):
		pass

	def test_update_contact(self):
		contact = Phonebook()
		response = contact.update_contact("Osoro", "03737373")
		self.assertEqual(response["message"], "Contact updated")
		pass
	def test_cannot_update_contact(self):
		pass

	def test_view_contact(self):
		contact = Phonebook()
		response = contact.view_contact()
		self.assertEqual(response["message"], "View contacts")
		pass
	def test_remove_contact(self):
		contact = Phonebook()
		response = contact.remove_contact("")
		self.assertEqual(response["message"], "Contact deleted")
		pass

