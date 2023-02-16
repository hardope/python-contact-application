import sqlite3
import sys
import cmd

class app(cmd.Cmd):

    prompt = "~ $ "

    def precmd(self, line):
        return line.strip().lower()

    def do_create(self, line):
        new_contact()

    def do_search(self, line):
        search_contacts(line)

    def do_help(self, line):
        help()

    def do_exit(self, line):
        sys.exit()

    def do_quit(self, line):
        sys.exit()

    def do_list(self, line):
        list_names()

    def do_delete(self, line):
        delete_contact(line)

    def emptyline(self):
        print()

def help():
    print("")
    print("COMMANDS")
    print("List: Display contact list.")
    print("New: To create a new contact.")
    print("Search: To search a contact.")
    print("Delete: To delete a contact.")
    print("Exit/Quit: To exit the app.\n")


def search_contacts(val):
    if val != "":
        search = val
    else:
        search = input("Search: ").strip()
    a = 0
    b = 0
    print("")
    print("Searching............")
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    

    cursor.execute(f"SELECT * FROM contacts WHERE names LIKE '%{search}%'")
    for row in (cursor.fetchall()):
        for column in row:
            if a == 0:
                print("Name: ",end="")
            if a == 1:
                print("Number: ",end="")
            if a == 2:
                print("E-mail: ",end="")
            print(column)
            b+=1
            a+=1
            if a == 2:
                a = 0
        print("")
    if b == 0:
        print("Not Found.\n")
    conn.commit()

    return
    
def new_contact():
    name = input("Name: ")
    if name == "":
        print("Invalid name")
        return
    cname = "contacts"

    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT count(names) FROM contacts WHERE names LIKE '%{name}&'")
    for row in(cursor.fetchall()):
        for column in row:
            if (int(column)) == 1:
                print("Contact Existing.")
                return
    number = input("Number: ")
    if number == "":
        print("Invalid Number")
        return
    email = input("E-mail: ")
    if email == "":
        print("Invalid E-Mail")
        return

    cursor.execute(f"INSERT INTO {cname} ('names', 'numbers', 'email') VALUES ('{name}', '{number}', '{email}')") 
    conn.commit()
    print("Saved.\n")
    return



def list_names():
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM contacts ORDER BY names""")
    for row in (cursor.fetchall()):
        a = 0
        for column in row:
            if a == 0:
                print("Name: ",end="")
            if a == 1:
                print("Number: ",end="")
            if a == 2:
                print("E-mail: ",end="")
            print(column)
            a+=1
        print("")

    conn.commit()

def delete_contact(val):
    if val != "":
        contact = val
    else:
        contact = input("Contact To Delete: ")
    print("Checking Contact............")

    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT count(names) FROM contacts WHERE names LIKE '{contact}'")
    for row in(cursor.fetchall()):
        for column in row:
            if (int(column)) == 1:
                print("Found contact......Deleting...")
            else:
                print("Contact is not existing.")
                return
    cursor.execute(f"DELETE FROM contacts WHERE names LIKE '{contact}'")
    print("Deleted.\n")

    conn.commit()
    return


if __name__ == "__main__":
    app().cmdloop()