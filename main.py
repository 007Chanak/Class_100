from ctypes import addressof

'''
name = "Chanak"
print(type(name))

info = []
print(type(info))

person = {

}
print(type(person))
'''

person = {
    "name": "Chanak",
    "mobile": 1234567890,
    "email": "xxxy@gmail.com",
    "address": "cwnaxx",
 
}
print(person["name"])

# Define Class
class Contact_Details:

    def __init__(self, name, mobile_number, email, address):
        self.contact_name = name
        self.contact_number = mobile_number
        self.email = email
        self.contact_address = address

        # Make a dictionary of the contact details 
        self.person = {
            "name": self.contact_name,
            "mobile" : self.contact_number,
            "email": self.email,
            "address": self.contact_address
        } 

    # Define the Methods of the class
    
    # View All Contact Details
    def view_contact_details(self, contact_list):
      print(contact_list)
      

    # Add the contact details to the list    
    def add_contact_details(self, contact_list):
      contact_list.append(self.person)

      new_contact = Contact_Details('Chanak',1234567890,'xxxy@gmail.com','cwnaxx')
      print(new_contact)

      def show_attributes(self):
        print(self.name) 
        print(self.email)
