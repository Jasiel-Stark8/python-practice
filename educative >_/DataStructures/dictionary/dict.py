# phone_book = dict([('Batman', 468426), ('Cersei', 237734), ('Ghostbusters', 44678)])
contact_name = int(input("Enter contact name(s): ").split(","))
contact_number = int(input("Enter contact number(s): ").split(","))

phone_book = dict(zip(contact_name, contact_number))

print(f"phone_book Contacts: {phone_book}")

try:
    print(phone_book.get([0]))

except ValueError:
    print("Contact not found")
