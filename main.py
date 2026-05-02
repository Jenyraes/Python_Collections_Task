# Problem 1: Bank Account

# Base class BankAccount
class BankAccount:
    
    # Constructor to initialize account number and balance
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance   # Private variable (Encapsulation)

    # Method to deposit money
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("Deposited:", amount)

    # Method to withdraw money
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        print("Withdrawn:", amount)

    # Property method to access private balance like an attribute
    @property
    def get_balance(self):
        return self.__balance


# SavingsAccount inherits BankAccount
class SavingsAccount(BankAccount):
    
    # Constructor with extra interest rate
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    # Method to calculate interest
    def Calculate_interest(self):
        interest = (self.get_balance * self.interest_rate) / 100
        print("Interest:", interest)


# CurrentAccount inherits BankAccount
class CurrentAccount(BankAccount):
    
    # Constructor with minimum balance
    def __init__(self, account_number, balance, min_balance):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    # Method to check minimum balance before withdrawal
    def withdrawal(self, amount):
        if self.get_balance - amount >= self.min_balance:
            super().withdraw(amount)
            print("Money can be withdrawn")
        else:
            print("Minimum balance must be maintained")


# Creating SavingsAccount object
s1 = SavingsAccount(1234, 10000, 5)

# Calculating interest
s1.Calculate_interest()

# Depositing money
s1.deposit(200)

# Withdrawing money
s1.withdraw(2000)


# Creating CurrentAccount object
c1 = CurrentAccount(5678, 20000, 500)

# Withdrawing money after checking minimum balance
c1.withdrawal(200)


# Problem 2: Employee Management

# Base class Employee
class Employee:
    
    # Constructor to initialize employee name and basic salary
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method to calculate salary (common for all employees)
    def calculate_salary(self):
        return self.salary


# RegularEmployee class inherits Employee
class RegularEmployee(Employee):
    
    # Constructor with extra bonus attribute
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    # Overriding salary calculation for regular employee
    def calculate_salary(self):
        return self.salary + self.bonus


# ContractEmployee class inherits Employee
class ContractEmployee(Employee):
    
    # Constructor with hours worked and rate per hour
    def __init__(self, name, salary, hours_worked, rate_perhour):
        super().__init__(name, salary)
        self.hours_worked = hours_worked
        self.rate_perhour = rate_perhour

    # Overriding salary calculation for contract employee
    def calculate_salary(self):
        return self.hours_worked * self.rate_perhour


# Manager class inherits Employee
class Manager(Employee):
    
    # Constructor with extra allowance attribute
    def __init__(self, name, salary, allowance):
        super().__init__(name, salary)
        self.allowance = allowance

    # Overriding salary calculation for manager
    def calculate_salary(self):
        return self.salary + self.allowance


# Creating object for RegularEmployee
s1 = RegularEmployee("Jack", 10000, 5000)

# Printing Jack's salary
print("Salary of Jack is:", s1.calculate_salary())


# Creating object for ContractEmployee
s2 = ContractEmployee("Heeman", 0, 10, 150)

# Printing Heeman's salary
print("Salary of Heeman is:", s2.calculate_salary())


# Creating object for Manager
s3 = Manager("Norman", 25000, 5000)

# Printing Norman's salary
print("Salary of Norman is:", s3.calculate_salary())


# Problem 3: Vehicle Rental

# Base class for all vehicles
class Vehicle:
    
    # Constructor to initialize model name and rental rate per day
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    # Method to calculate basic rental cost
    def calculate_rental(self, days):
        return self.rental_rate * days


# Car class inherits Vehicle class
class Car(Vehicle):
    
    # Constructor with extra attribute seats
    def __init__(self, model, rental_rate, seats):
        super().__init__(model, rental_rate)
        self.seats = seats

    # Overriding rental calculation for Car
    def calculate_rental(self, days):
        return (self.rental_rate * days) + (self.seats * 100)


# Bike class inherits Vehicle class
class Bike(Vehicle):
    
    # Constructor with extra attribute helmet charge
    def __init__(self, model, rental_rate, helment_charge):
        super().__init__(model, rental_rate)
        self.helment_charge = helment_charge

    # Overriding rental calculation for Bike
    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.helment_charge


# Truck class inherits Vehicle class
class Truck(Vehicle):
    
    # Constructor with extra attribute load charge
    def __init__(self, model, rental_rate, load_charge):
        super().__init__(model, rental_rate)
        self.load_charge = load_charge

    # Overriding rental calculation for Truck
    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.load_charge


# Creating Car object
car = Car("Swift", 1000, 5)

# Printing Car rental for 3 days
print(car.calculate_rental(3))


# Creating Bike object
bike = Bike("Yamaha", 500, 200)

# Printing Bike rental for 2 days
print(bike.calculate_rental(2))


# Creating Truck object
truck = Truck("Tata", 1500, 2000)

# Printing Truck rental for 3 days
print(truck.calculate_rental(3))