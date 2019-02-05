class Account:
    def __init__(self):
        print("I'm self method")
    def Meta(self,address):
        print(address)

account = Account()
account.Meta("Dhaka, Bangladesh")
