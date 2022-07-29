# web-based-contact-application

### Steps on installation
* Download file
* Unzip file
* Save file to directory
* Open command-line
* make sure python is installed

#### Description:
This is a python command-line based contact application that enables you to store, search, delete, list and create contacts. This application uses python for operations and SQL database for storage. 

### phoneapp.py

#### def main():

This is the main function, when running it asks for input of option from user and call functions according to the options provided by user. This program continues to run until the user inputs 'exit' or 'quit' case insensitively.

#### def search_contacts(name):

This function takes an argument which is a name of a contact to be searched, the function searches the database by running SQL queries and prints all matching contacts.

#### def list_names():

This function queries the database for all contacts, it then stores all the results for cleaning and formating before prints all existing contacts.

#### def new_contact(name, number, email):

This function takes three arguements(name, number, email) provided by user, then it inputs the data into the satabase using SQL queries while checking for errors and wrong input.

#### def delete_contact(name):

This function only takes name as arguement, checks the database to see if contact exists and then deletes it if it does.

 
