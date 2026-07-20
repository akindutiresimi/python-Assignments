#ask the driver for input 
#also the efficency of the car 
#enter the price per gallon 


distance = float(input("distance"))
mile_gallon = float(input("gallon"))
cost = float(input("cost"))
cost_driving = float((distance / mile_gallon) * cost)
print(cost_driving)