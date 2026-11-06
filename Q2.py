# Q2. Secure Bank Account - Encapsulation

class BankAccount:
    def __init__(self, account_holder, pin, opening_balance=0):
        if not isinstance(opening_balance, (int, float)) or opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.account_holder = account_holder
        self.__balance = opening_balance
        self.__pin = str(pin)

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            print("Deposit rejected: amount must be positive.")
            return False
        self.__balance += amount
        print(f"Deposit successful: Rs. {amount:,.2f}")
        return True

    def withdraw(self, amount, pin):
        if str(pin) != self.__pin:
            print("Withdrawal rejected: incorrect PIN.")
            return False
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            print("Withdrawal rejected: amount must be positive.")
            return False
        if amount > self.__balance:
            print("Withdrawal rejected: insufficient balance.")
            return False
        self.__balance -= amount
        print(f"Withdrawal successful: Rs. {amount:,.2f}")
        return True

    def get_balance(self, pin):
        if str(pin) != self.__pin:
            print("Balance access denied: incorrect PIN.")
            return None
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Ali", "2468", 5000)
    second_account = BankAccount("Sara", "1357", 2500)

    account.deposit(2000)
    account.withdraw(1500, "2468")
    account.withdraw(1000, "0000")   # Rejected: wrong PIN
    account.withdraw(10000, "2468") # Rejected: insufficient funds

    print(f"{account.account_holder}'s balance: Rs. {account.get_balance('2468'):,.2f}")
    print(f"{second_account.account_holder}'s balance: Rs. {second_account.get_balance('1357'):,.2f}")

    # Double underscores trigger name mangling; they discourage accidental access,
    # but do not provide encryption or strong security in Python.
