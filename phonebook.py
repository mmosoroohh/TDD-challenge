import uuid

class Phonebook():

	def __init__(self):
		self.user_info = {}
		
		

	def create_contact(self, name, number):
		self.user_info[name]= number
		return {"message": "Contact created"}

	def update_contact(self, name, number):
		self.user_info[name] = number
		return {"message": "Contact updated"}

	def view_contact(self):
		self.user_info = Phonebook
		return {"message": "View contacts"}


	def remove_contact(self, name):
		self.user_info = name		
		return{"message": "Contact deleted"}