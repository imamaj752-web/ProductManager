class BankAccount:
    def __init__(self, initial_balance=0, interest_rate=0.01):
        self.__balance = initial_balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"ПОПОЛНЕНИЯ: +{amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"СНИМАЮТ: -{amount}")

    def add_interest(self):
        inteest = self.__balance * self.__interest_rate
        self.__balance += inteest
        self.__transactions.append(f"ПРОЦЕНТ: +{inteest:.2f}")

    def history(self):
        for t in self.__transactions:
            print(t)
        print(f"БАЛАНС: {self.__balance:.2f}")