import csv

contacts = []

def save_contacts():
    with open('A.csv', 'w',newline='') as file:
        header_names = ['Name','Phone','Email','Address']
        writer = csv.DictReader(file, fieldnames=header_names)

        writer.writeheader()
        writer.writerows(contacts)



def view_contacts():
    print('Your Address Book:')       
    for contact in contacts:
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
        print(f"Address: {contact['Address']}")
        print("-" * 30)
 
def open_file():
    try:
        with open('A.csv' , 'r') as file:
            lines = csv.DictReader(file)
            for line in lines:
                contacts.append(line)
    except FileNotFoundError:
        print('This file does not exist!')

open_file()
while True:
    try:
        print('Address Book Menu:')
        print('1. Add Contact')
        print('2. View Contact')
        print('3. Update Contact')
        print('4. Delet Contact')
        print('5. Exit')

        choice = int(input("Enter your choice (1/2/3/4/5): ").strip())

        if choice == 2:
             view_contacts()
        elif choice == 5:
             print('goodbye')    
             exit()
        else:
            print("invalied choies")        

    except Exception as e:
        print(f'error:{e}')
       
# import csv

# contacts = [{'Name': 'Ali', 'Phone': '1234567890', 'Email': 'ali@example.com', 'Address': 'Tehran'}]

# def save_contacts():
#     with open('A.csv', 'w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=['Name', 'Phone', 'Email', 'Address'])
#         writer.writeheader()
#         writer.writerows(contacts)

# save_contacts()
# print("Contacts saved successfully!")
