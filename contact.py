# Import the regular expression library for validating phone numbers and emails
import re
# Import the datetime module to record creation and update times of contacts
from datetime import datetime

# Define a class named Contact to store and manage contact information
class Contact:
    # Initialize method, called when a new Contact object is created
    def __init__(self, first_name, last_name, phone_number, email=None, address=None):
        # Accepts first name, last name, phone number, email (optional), and address (optional) as parameters
        self.first_name = first_name  # Store the first name
        self.last_name = last_name  # Store the last name
        self.phone_number = self.validate_phone_number(phone_number)  # Validate and store the phone number
        self.email = self.validate_email(email)  # Validate and store the email (if provided)
        self.address = address  # Store the address (if provided)
        self.created_at = datetime.now()  # Record the creation time
        self.updated_at = datetime.now()  # Record the update time (initially the same as creation time)
        self.history = []  # Initialize an empty history list

    # Method to validate the phone number
    # Accepts a phone number string as a parameter and returns the validated phone number
    def validate_phone_number(self, phone_number):
        digits = re.findall(r'\d', phone_number)  # Extract all digits using regular expressions
        if len(digits) < 10:  # If there are fewer than 10 digits, raise an exception
            raise ValueError("Phone number must contain at least 10 digits")
        return ''.join(digits[-10:])  # Return the last 10 digits as the phone number

    # Method to validate the email address
    # Accepts an email string as a parameter and returns the validated email (if valid)
    def validate_email(self, email):
        if email:  # If an email address is provided
            pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')  # Define a regex pattern for email validation
            if not pattern.match(email):  # If the email does not match the pattern, raise an exception
                raise ValueError("Invalid email address")
        return email  # Return the validated email address (or None if not provided)

    # Method to format the phone number into (XXX) XXX-XXXX format
    def formatted_phone_number(self):
        return f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"

    # Define __str__ method to return a string representation of the object
    # This method is called when using print() on the object or converting it to a string
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.formatted_phone_number()}, {self.email}, {self.address}"