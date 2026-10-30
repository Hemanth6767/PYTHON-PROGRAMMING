
password = input("Enter password: ")

if len(password) >= 8:
    print("Password length is valid")
else:
    print("Password must contain 8 characters")

if any(ch.isdigit() for ch in password):
    print("Contains a number")
else:
    print("Must contain a number")

if any(ch.isalpha() for ch in password):
    print("Contains a letter")
else:
    print("Must contain a letter")
