import numpy as np
fuel_efficiency=np.array([23,45,36,78])
average=np.mean(fuel_efficiency)
percentage=((fuel_efficiency[3]-fuel_efficiency[1])/(fuel_efficiency[0])*100)
print("average fuel efficiency",average)
print("percentage of fuel",percentage)
