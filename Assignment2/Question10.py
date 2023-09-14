# Q.10 write a function to return compound interest

def calculate_compound_interest(p, n, r=8.5):
    ci = p * ( 1 -  ((r/100)) ** n) - p
    print(f"ci is {ci}")

calculate_compound_interest(20, 40, 60)