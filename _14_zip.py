first_name = ["Tawhiduzzaman" , "Arifuzzaman" , "Kamruzzaman" , "Moniruzzaman"]
last_name  = ["Turag" , "Tanin" , "Munna" , "Moni"]
phone = ["No Phone" , "Iphone 5s", "MI A2" , "POCO Phone"]

_zip = zip(first_name , last_name, phone)

for f,l,p in _zip:
    print(f,l,p)


# Tawhiduzzaman Turag No Phone
# Arifuzzaman Tanin Iphone 5s
# Kamruzzaman Munna MI A2
# Moniruzzaman Moni POCO Phone