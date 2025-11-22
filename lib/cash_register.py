#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=None):
        self.discount = discount if discount is not None else 0
        self.total = 0
        self.items = []
        self.last_transaction = 0
        self.last_items = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if value is None:
            self._discount = 0
        else:
            self._discount = value

    def add_item(self, title, price, quantity=1):
        if not (isinstance(price, (int, float)) and isinstance(title, str)):
            raise ValueError("Price must be a number and Title must be a string")
        self.last_transaction = price * quantity
        self.last_items = [title] * quantity
        self.items.extend(self.last_items)
        self.total += self.last_transaction
        return self.total

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        for item in self.last_items:
            if item in self.items:
                self.items.remove(item)
        self.last_transaction = 0
        self.last_items = []
