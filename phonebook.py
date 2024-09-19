import csv
import logging
from datetime import datetime
from contact import Contact

class PhoneBook:
    def __init__(self):
        # Initialize the phone book with an empty list of contacts and configure logging
        self.contacts = []
        logging.basicConfig(filename='phonebook.log', level=logging.INFO)

    def add_contact(self, contact):
        # Add a new contact to the phone book and log the action
        self.contacts.append(contact)
        logging.info(f"{datetime.now()}: Added contact: {contact}")

    def view_contacts(self):
        # Print all contacts in the phone book
        for contact in self.contacts:
            print(contact)

    def search_contacts(self, query, search_type):
        # Search contacts based on name or phone number
        if search_type == 'name':
            results = [contact for contact in self.contacts if query.lower() in (contact.first_name.lower() + ' ' + contact.last_name.lower())]
        elif search_type == 'phone':
            query_digits = ''.join(char for char in query if char.isdigit())
            results = [contact for contact in self.contacts if query_digits in ''.join(char for char in contact.phone_number if char.isdigit())]
        else:
            print("Invalid type of search, please enter 'name' or 'phone'.")
            return []
        if not results:
            print("No matching contacts found.")
        return results

    def search_contacts_by_date(self, start_date, end_date):
        # Search contacts created within a specific date range
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter dates in YYYY-MM-DD format.")
            return []
        results = [contact for contact in self.contacts if start_date <= contact.created_at <= end_date]
        return results

    def update_contact(self, old_contact, new_contact):
        # Update an existing contact with new information and log the change
        index = self.contacts.index(old_contact)
        self.contacts[index] = new_contact
        logging.info(f"{datetime.now()}: Updated contact: {old_contact} to {new_contact}")

    def delete_contact(self, contact):
        # Remove a contact from the phone book and log the action
        self.contacts.remove(contact)
        logging.info(f"{datetime.now()}: Deleted contact: {contact}")

    def import_contacts_from_csv(self, file_path):
        # Import contacts from a CSV file and add them to the phone book
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                try:
                    contact = Contact(*row)
                    self.add_contact(contact)
                except ValueError as e:
                    print(f"Skipping row due to error: {e}")
    
    def sort_contacts(self, by='last_name'):
        # Sort contacts based on a specified attribute (default is 'last_name')
        self.contacts.sort(key=lambda contact: getattr(contact, by))

    def group_contacts(self):
        # Group contacts by the initial letter of their last name
        groups = {}
        for contact in self.contacts:
            initial = contact.last_name[0].upper()
            if initial not in groups:
                groups[initial] = []
            groups[initial].append(contact)
        return groups