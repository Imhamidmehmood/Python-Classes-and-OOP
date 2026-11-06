# Q8. Payment Gateway - Abstraction

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    @staticmethod
    def validate_amount(amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            raise ValueError("Transaction amount must be a positive number.")


class CardPayment(PaymentMethod):
    def pay(self, amount):
        self.validate_amount(amount)
        print(f"Card Payment | Payment | Rs. {amount:,.2f}")

    def refund(self, amount):
        self.validate_amount(amount)
        print(f"Card Payment | Refund | Rs. {amount:,.2f}")


class WalletPayment(PaymentMethod):
    def pay(self, amount):
        self.validate_amount(amount)
        print(f"Wallet Payment | Payment | Rs. {amount:,.2f}")

    def refund(self, amount):
        self.validate_amount(amount)
        print(f"Wallet Payment | Refund | Rs. {amount:,.2f}")


class BankTransferPayment(PaymentMethod):
    def pay(self, amount):
        self.validate_amount(amount)
        print(f"Bank Transfer | Payment | Rs. {amount:,.2f}")

    def refund(self, amount):
        self.validate_amount(amount)
        print(f"Bank Transfer | Refund | Rs. {amount:,.2f}")


def process_transaction(payment_method, amount):
    payment_method.pay(amount)


if __name__ == "__main__":
    methods = [CardPayment(), WalletPayment(), BankTransferPayment()]

    for method in methods:
        process_transaction(method, 2500)

    methods[0].refund(500)

    try:
        process_transaction(methods[1], -100)
    except ValueError as error:
        print(f"Invalid transaction: {error}")

    # A new class can implement PaymentMethod and work with
    # process_transaction() without changing that function.
