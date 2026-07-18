contacts={}
running=True

def add_contact():
    name=input("Enter name:")
    number=input("Enter number:")

    if name not in contacts:
        contacts[name]=number
        print(name,":",number)
    else:
        print("Contact already exists.")

def view_contact():
    
    if contacts:
        for name,number in contacts.items():
            print(name,":",contacts[name])
    else:
        print("No contacts available.")

def search_contact():
    name=input("Enter a name:")

    if name in contacts:
        print("Contact found.")
    else:
        print("Not found.")

def delete_contact():
    name=input("Enter name:")

    if name in contacts:
        del contacts[name]
        print("Deleted successfully.")
    else:
        print("No contact available.")

while running:
    print("\n ====== CONTACT BOOK ======")
    
    print("1.Add contact")
    print("2.view contact")
    print("3.Search contact")
    print("4.Delete contact")
    print("5.Exit")

    user=int(input("Enter your choice:"))

    if user==1:
        add_contact()

    elif user==2:
        view_contact()

    elif user==3:
        search_contact()

    elif user==4:
        delete_contact()

    elif user==5:
        running=False
        print("THANKYOU !!")
        
    else:
        print("Invalid choice.")
        