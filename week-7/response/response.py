import validators

e = input("What's your email address? ")
if validators.email(e):
    print("Valid")
else:
    print("Invalid")
