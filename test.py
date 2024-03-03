in_amount=float(input("Enter the investment amount: "))
years=int(input("Enter the number of years: "))
rate=int(input("Enter the rate as a %: "))
print("Year Starting balance Interest Ending balance")
sb=in_amount
for i in range(1,years+1):
    interest=(rate/100)*sb
    eb=sb+interest
    print('%4s' % i,'%15.2f' % sb,'%9.2f' % interest,'%7.2f' % eb)
    sb=eb