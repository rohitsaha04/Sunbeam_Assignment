# Q9. write a function to return simple interest 

def calculate_simple_interest(p, n, r=8.5):
    si = (p * n * r ) / 100
    print(si)

calculate_simple_interest(20, 40, 60)