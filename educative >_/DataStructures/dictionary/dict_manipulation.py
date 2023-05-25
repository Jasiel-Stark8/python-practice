phone_book = {
    "Batman": 468426,
    "Cersei": 237734,
    "Ghostbusters": 44678
    }
phone_book.update({"Batman": 468429})
phone_book.update({"Godzilla": 242203})
print(phone_book)

# Delete key from database
phone_book.pop("Batman")
print(phone_book)

print("Batman" in phone_book)
print("Godzilla" in phone_book)
print(len(phone_book))
