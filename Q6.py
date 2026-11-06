# Q6. Checkout Discount Calculator - Polymorphism

class Customer:
    DISCOUNT_RATE = 0.0

    def final_price(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount < 0:
            raise ValueError("Bill amount cannot be negative and must be numeric.")
        return amount * (1 - self.DISCOUNT_RATE)


class RegularCustomer(Customer):
    DISCOUNT_RATE = 0.05


class PremiumCustomer(Customer):
    DISCOUNT_RATE = 0.10


class VIPCustomer(Customer):
    DISCOUNT_RATE = 0.20


class GoldCustomer(Customer):
    DISCOUNT_RATE = 0.15


def print_receipt(customer, amount):
    final_amount = customer.final_price(amount)
    print(f"{customer.__class__.__name__}: Rs. {final_amount:,.2f}")


if __name__ == "__main__":
    bill = 10000
    customers = [
        RegularCustomer(),
        PremiumCustomer(),
        VIPCustomer(),
        GoldCustomer()
    ]

    for customer in customers:
        print_receipt(customer, bill)

    try:
        print_receipt(RegularCustomer(), -500)
    except ValueError as error:
        print(f"Invalid bill: {error}")

    # GoldCustomer is added without changing print_receipt().
