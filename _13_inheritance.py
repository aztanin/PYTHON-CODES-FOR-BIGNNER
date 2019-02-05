class Education:
    def Degree(self,degreeName):
        print(degreeName)

class Hobby:
    def MyHobby(self,hobbyName):
        print(hobbyName)

class Account(Education, Hobby):
    def __init__(self):
        print("I'm self method")
    def Meta(self,address):
        print(address)

account = Account()
account.Meta("Dhaka, Bangladesh")
account.Degree("B.Sc")
account.MyHobby("I've not any hobby")
