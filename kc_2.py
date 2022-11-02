


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

bikeData = pd.read_csv('assets/bike_details.csv')
print(bikeData)

plt.plot(bikeData['name'],bikeData['selling_price'], '^')
plt.title("Motorcycle Prices", fontsize=24)
plt.xlabel("Motorcycle Model", fontsize=18)
plt.ylabel("Price", fontsize=18)
plt.show()





