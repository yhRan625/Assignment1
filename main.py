import sys
from phonebook import PhoneBook
from contact import Contact

def main():
    """
    The main function of the Phone Book Manager application.
    It provides a command-line interface for users to interact with the application.
    """
    phonebook = PhoneBook()  # Create an instance of PhoneBook to manage contacts

    while True:
        # Display the main menu options
        print("\nPhone Book Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Import Contacts from CSV")
        print("7. Search Contacts by Date")
        print("8. Exit")

        choice = input("Enter your choice: ")  # Get user input for menu choice

        if choice == '1':
            # Add a new contact
            while True:
                try:
                    # Get contact details from user
                    first_name = input("First Name: ")
                    last_name = input("Last Name: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email (Optional): ")
                    address = input("Address (Optional): ")
                    # Create a new Contact object and add it to the phonebook
                    contact = Contact(first_name, last_name, phone_number, email, address)
                    phonebook.add_contact(contact)
                    break
                except ValueError as e:
                    # Handle any errors during contact creation
                    print(f"Error: {e}. Please try again.")
        elif choice == '2':
            # View all contacts, grouped by the first letter of the last name
            groups = phonebook.group_contacts()
            for initial in sorted(groups.keys()):
                print(f"\nGroup {initial}:")
                for contact in groups[initial]:
                    print(contact)
            
        elif choice == '3':
            # Search for contacts by name or phone number
            query = input("Enter search query: ")
            search_type = 'phone' if query.isdigit() else 'name'
            results = phonebook.search_contacts(query, search_type)
            for contact in results:
                print(contact)
        elif choice == '4':
            # Update an existing contact
            query = input("Enter search query: ")
            search_type = 'phone' if ''.join(char for char in query if char.isdigit()).isdigit() else 'name'
            results = phonebook.search_contacts(query, search_type)
            if not results:
                continue
            for contact in results:
                print(contact)
            update_choice = input("Enter the name or phone number of the contact to update: ")
            update_search_type = 'phone' if ''.join(char for char in update_choice if char.isdigit()).isdigit() else 'name'
            update_results = phonebook.search_contacts(update_choice, update_search_type)
            if update_results:
                # Get updated contact details from user
                new_first_name = input("New First Name: ")
                new_last_name = input("New Last Name: ")
                new_phone_number = input("New Phone Number: ")
                new_email = input("New Email (Optional): ")
                new_address = input("New Address (Optional): ")
                try:
                    # Create a new Contact object and update the existing contact
                    new_contact = Contact(new_first_name, new_last_name, new_phone_number, new_email, new_address)
                    phonebook.update_contact(update_results[0], new_contact)
                    print("Contact updated.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("No matching contact found.")

        elif choice == '5':
            # Delete one or more contacts
            delete_choice = input("Enter the names or phone numbers of the contacts to delete (separated by commas): ")
            delete_choices = delete_choice.split(',')
            for choice in delete_choices:
                choice = choice.strip()
                delete_search_type = 'phone' if ''.join(char for char in choice if char.isdigit()).isdigit() else 'name'
                delete_results = phonebook.search_contacts(choice, delete_search_type)
                if delete_results:
                    phonebook.delete_contact(delete_results[0])
                    print(f"Contact {choice} deleted.")
                else:
                    print(f"No matching contact found for {choice}.")
        elif choice == '6':
            # Import contacts from a CSV file
            file_path = input("Enter CSV file path: ")
            phonebook.import_contacts_from_csv(file_path)

        elif choice == '7':
            # Search for contacts by date range
            while True:
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                results = phonebook.search_contacts_by_date(start_date, end_date)
                if results != "Invalid":
                    break
            for contact in results:
                print(contact)

        elif choice == '8':
            # Exit the application
            sys.exit()

        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choices

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly