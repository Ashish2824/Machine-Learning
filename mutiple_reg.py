import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('D:\UPES - 4 Sem\LAB WORK\ML\lab2\MRdata.csv')
print(data)

X = data[['Age', 'Milage']]
Y = data['Price']

plt.scatter(X['Age'], Y)
plt.scatter(X['Milage'], Y)
plt.show()


c = 32.46
m1 = -1.54
m2 = -0.15

Y_pred = c + m1*data['Age'] + m2*data['Milage']

plt.scatter(X['Age'], Y)
plt.scatter(X['Milage'], Y) # actual (DATA)

# plt.scatter(X, Y_pred, color='red')
plt.plot([min(data['Age']), max(data['Age'])], [min(data['Milage']), max(data['Milage'])], [min(Y_pred), max(Y_pred)], color='red') # Predicted Values
plt.show()


error = Y-Y_pred
print(error)

sq_er = error*error
print(sq_er)


