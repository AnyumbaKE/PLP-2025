#! /usr/bin/env python3

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# calculate the final price
final_price = calculate_discount(price, discount_percent)

# display the result
if discount_percent >= 20:
    print(f"The final price after a {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The final price is: {final_price}")