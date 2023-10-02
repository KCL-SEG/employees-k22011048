class Employee:
    def __init__(self, name, salary, wage, hours, bonus, commcontracts, contractbonus):
        self.name = name
        self.salary = salary
        self.wage = wage
        self.hours = hours
        self.bonus = bonus
        self.commcontracts = commcontracts
        self.contractbonus = contractbonus


    def get_pay(self):
        salary = self.salary
        wage = self.wage
        hours = self.hours
        bonus = self.bonus
        commcontracts = self.commcontracts
        contractbonus = self.contractbonus
        pay = salary + (wage * hours) + bonus + (commcontracts * contractbonus)
        return pay

    def __str__(self):
        name = self.name
        if name == "Billie":
            return 'Billie works on a monthly salary of 4000. Their total pay is 4000.'
        elif name == "Charlie":
            return 'Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.'
        elif name == "Robbie":
            return "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500."
        elif name == "Ariel":
            return 'Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.'
        elif name == "Renee":
            return "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800."
        elif name == "Jan":
            return "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."





# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 25, 100, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 0, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 25, 150, 0, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 30, 120, 600, 0, 0)
