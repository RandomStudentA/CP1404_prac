email_list = {}
email = input("Email: ")

def name_is(email):
    parts = email.split('@')[0]
    email = parts.split('.')
    name = " ".join(parts).title()


email = input("Email: ")

if email != "":
    name = name_is(email)
    identify = input("Is your name {}? (Y/n) ".format(name))
    if identify.upper() != "Y" and identify != "":
        email = input("Email: ")
        name = input("Name: ")
        name_is[email] = name
    else:
        print('Error')
    for email, name in name_is().items():
        print(name, email)
else:
    print('Error')


