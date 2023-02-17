import sqlite3
import sys
import cmd

class app(cmd.Cmd):

    prompt = " ~ $ "

    def precmd(self, line):
        return line.strip().lower()

    def do_create(self, line):
        new_contact(line)

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
    print("Search <query>: To search a contact named query.")
    print("Delete <query>: To delete a contact named query.")
    print("Exit/Quit: To exit the app.\n")


def search_contacts(val):
    if val != "":
        search = val
    else:
        search = input("Search Name: ").strip()
    a = 0
    b = 0
    print("")
    print("Searching............")
    names = query_db(f"SELECT * FROM contacts WHERE names LIKE '%{search}%'")
    for row in (names):
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

    return
    
def new_contact(val):
    try:
        val = val.split(" ")
        count = 0
        my_dict = {}
        for i in val:
            count+=1
            i = i.split("=")
            my_dict[i[0].strip()] = i[1].strip()
        assert count > 2

        name = my_dict["name"]
        number = my_dict["number"]
        email = my_dict["email"]

        assert name != ""
        assert number != ""
        assert email != ""

    except:
        name = input("Name: ")
        if name == "":
            print("Invalid name")
            return

        number = input("Number: ")
        if number == "":
            print("Invalid Number")
            return
        email = input("E-mail: ")
        if email == "":
            print("Invalid E-Mail")
            return

    check = query_db(f"SELECT count(names) FROM contacts WHERE names == '{name}'")
    if check[0][0] > 0:
                print("Contact Existing.")
                return

    query_db(f"INSERT INTO contacts ('names', 'numbers', 'email') VALUES ('{name}', '{number}', '{email}')")
    print("Saved.\n")
    return

def list_names():
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()

    names = query_db("SELECT * FROM contacts ORDER BY names")
    for row in (names):
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

def delete_contact(val):
    if val != "":
        contact = val
    else:
        contact = input("Contact To Delete: ")
    print("Checking Contact............")

    check = query_db(f"SELECT count(names) FROM contacts WHERE names LIKE '{contact}'")
    if check[0][0] > 0:
        print("Found contact......Deleting...")
    else:
        print("Contact is not existing.")
        return
    query_db(f"DELETE FROM contacts WHERE names LIKE '{contact}'")
    print("Deleted.\n")
    return

def query_db(query):
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    return cursor.fetchall()


if __name__ == "__main__":
    app().cmdloop()