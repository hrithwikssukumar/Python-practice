

class Account:
    def __init__(self,account_number,account_balance):
        self.account_number = account_number
        self.account_balance = account_balance

    def withdraw(self,amount):
        if self.account_balance-amount > 0:
            self.account_balance = self.account_balance - amount
        else:
            print("Withdrawal failed")    

    def display(self):
        print("Your account balance is {}".format(self.account_balance))

account_1 = Account("A12345",10000)
account_2 = Account("B45678",15000)

amount = int(input("enter the amount to withdraw from account 2"))
account_2.withdraw(amount)
account_2.display()






class Player:
    extra_runs=1000
    def __init__(self, name, jersey_no, odi, t20, test):
        self.name = name
        self.jersey_no = jersey_no
        self.odi = odi
        self.t20 = t20
        self.test = test

    def find_total(self):
        self.total = self.odi + self.t20 + self.test + self.extra_runs
        print("Total runs scored by {} is {}".format(self.name, self.total))

        

player_1 = Player("Virat", 18, 1000, 2600, 3200)
player_2 = Player("Rohit", 45, 2000, 1000, 2400)
player_3 = Player("Hardik", 33, 1200, 2500, 1600)

Player.extra_runs(239)
player_1.find_total()
player_2.find_total()
player_3.find_total()




    



# Class method

class Player:
    extra_runs=1000
    def __init__(self, name, jersey_no, odi, t20, test):
        self.name = name
        self.jersey_no = jersey_no
        self.odi = odi
        self.t20 = t20
        self.test = test

    def find_total(self):
        self.total = self.odi + self.t20 + self.test + self.extra_runs
        print("Total runs scored by {} is {}".format(self.name, self.total))

    @classmethod
    def change_extra_runs(cls,extra_runs):
        cls.extra_runs = cls.extra_runs + extra_runs

        

player_1 = Player("Virat", 18, 1000, 2600, 3200)
player_2 = Player("Rohit", 45, 2000, 1000, 2400)
player_3 = Player("Hardik", 33, 1200, 2500, 1600)

Player.extra_runs(239)
player_1.find_total()
player_2.find_total()
player_3.find_total()

