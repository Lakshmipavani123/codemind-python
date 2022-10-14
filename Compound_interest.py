def compound_interest(principle, rate, time):
 
    # Calculates compound interest
    CI = principle * (pow((1 + rate / 100), time))
    print('%0.2f'%CI)
 
x,y,z=map(int,input().split())
compound_interest(x, y, z)
