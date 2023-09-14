# Question7 Write a program that will calculate the price for a quantity entered from the keyboard, given that the unit
# price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15 percent discount for qu
# antities over 50.

def price():
    quantity = int(input("Enter Quantity "))
    total_price = quantity * 5
    if(total_price >= 30 and total_price <= 50):
        discount_price = total_price / 10
        print(f" You have charged {discount_price}")
    else:
        discount_price = total_price / 15
        print(f"You have charged {discount_price}")

price()