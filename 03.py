import numpy as np
beds=np.array([4,2,5,3])
price=np.array([25000,34000,22000,32000])
square=np.array([23,24,56,34])
average_beds=price[beds>4]
average_price=np.mean(average_beds)
print("average of the sale price",average_price)
