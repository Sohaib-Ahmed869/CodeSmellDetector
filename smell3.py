# Another deliberately smelly code example with different code smells
import random
import string


# God Class - Handling both user management and payment processing
class SystemManager:
    def __init__(self):
        self.users = []
        self.payments = []

    # Long Method - Does multiple things: adds user, validates, updates user, prints summary
    def add_user(self, username, age, email, country, password, balance, user_type):
        if len(username) < 3:
            print("Username is too short!")
            return

        if age < 18:
            print("User must be at least 18 years old.")
            return

        if '@' not in email:
            print("Invalid email format!")
            return

        if balance < 0:
            print("Balance can't be negative.")
            return

        user = {
            "username": username,
            "age": age,
            "email": email,
            "country": country,
            "password": password,
            "balance": balance,
            "user_type": user_type
        }

        self.users.append(user)
        print(f"User {username} added successfully.")

        # Updating user details and printing user information - unrelated to adding user
        if user_type == "premium":
            user["bonus"] = balance * 0.05
        else:
            user["bonus"] = 0

        print(f"User Summary: {user}")

    # Large Parameter List - Excessive arguments for a single function
    def process_payment(self, payer_name, payee_name, amount, payment_type, currency, discount=0, tax=0,
                        payment_method="credit card", transaction_fee=0):
        payer = None
        payee = None
        for user in self.users:
            if user["username"] == payer_name:
                payer = user
            elif user["username"] == payee_name:
                payee = user

        if payer is None or payee is None:
            print("Payer or Payee not found.")
            return

        total_amount = amount - discount + tax + transaction_fee
        if payer["balance"] >= total_amount:
            payer["balance"] -= total_amount
            payee["balance"] += amount
            self.payments.append(
                {"payer": payer_name, "payee": payee_name, "amount": amount, "payment_type": payment_type})
            print(f"Payment of {total_amount} {currency} from {payer_name} to {payee_name} successful.")
        else:
            print("Insufficient balance!")

    # Duplicated Code - Payment processing logic is copied again with minor changes
    def process_payment_vip(self, payer_name, payee_name, amount, payment_type, currency, vip_discount=10):
        payer = None
        payee = None
        for user in self.users:
            if user["username"] == payer_name:
                payer = user
            elif user["username"] == payee_name:
                payee = user

        if payer is None or payee is None:
            print("Payer or Payee not found.")
            return

        total_amount = amount - vip_discount
        if payer["balance"] >= total_amount:
            payer["balance"] -= total_amount
            payee["balance"] += amount
            self.payments.append(
                {"payer": payer_name, "payee": payee_name, "amount": amount, "payment_type": payment_type})
            print(f"VIP Payment of {total_amount} {currency} from {payer_name} to {payee_name} successful.")
        else:
            print("Insufficient balance!")

    # Long Method - Adds product, calculates total cost, updates stock, prints summary
    def add_product(self, product_name, price, stock, discount, tax):
        if price < 0 or stock < 0:
            print("Invalid price or stock.")
            return

        product = {
            "product_name": product_name,
            "price": price,
            "stock": stock,
            "discount": discount,
            "tax": tax
        }

        total_price = price - discount + tax
        product["total_price"] = total_price
        print(f"Product Summary: {product}")

    # Large Parameter List - Excessive arguments
    def update_product(self, product_name, price, stock, discount, tax, seller_name, seller_rating, country_of_origin,
                       warranty_period, return_policy):
        print(f"Updating product: {product_name}")
        # Dummy update logic
        print(f"Product updated with price {price}, stock {stock}")


def main():
    manager = SystemManager()

    # Adding users
    manager.add_user("alice", 25, "alice@mail.com", "USA", "securepass123", 1000, "premium")
    manager.add_user("bob", 17, "bob@mail.com", "UK", "password456", 500, "regular")

    # Processing payments with large parameter lists
    manager.process_payment("alice", "bob", 100, "online", "USD", discount=10, tax=5, payment_method="debit card",
                            transaction_fee=2)
    manager.process_payment_vip("alice", "bob", 100, "online", "USD")

    # Adding products
    manager.add_product("Laptop", 800, 10, 50, 30)
    manager.update_product("Laptop", 750, 8, 40, 20, "BestSeller", 5, "China", "2 years", "30 days")


if __name__ == "__main__":
    main()
