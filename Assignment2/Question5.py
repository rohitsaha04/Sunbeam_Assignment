# Q5. Write a program that prompts the user to input number of calls and calculate the monthly telephone bills
# as per the following rule: 
 
# Minimum Rs. 200 for up to 100 calls. 
# Plus Rs. 0.60 per call for next 50 calls. 
# Plus Rs. 0.50 per call for next 50 calls. 
# Plus Rs. 0.40 per call for any call beyond 200 calls.

def calculate_calls():
    calls = int(input("Enter any number "))
    if(calls <= 100):
        print("You are charged 200 Rs")
    elif(calls <= 150):
       charged = calls * 0.60
       print(f"You are charged {charged} Rs")
    elif(calls <= 200):
        charged = calls * 0.50
        print(f"You are Charged {charged} Rs")
    else:
        charged = calls * 0.40
        print(f"You are charged {charged} Rs")

calculate_calls()
    