from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np  

Path = "city info/formatted/turkiye.csv"
df = pd.read_csv(Path)
prediction_years = [2023, 2028]

df["Ratio"] = df["Female MP Count"].values/df["Total Count"].values
feature = df["Ratio"].values
label = df["Female MP Count"].values
feature = feature.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(feature, label, test_size=6/27, random_state=42, shuffle=False)

reg = LinearRegression().fit(X_train, y_train)

y_pred = reg.predict(X_test)

y_pred_train = reg.predict(X_train)

mse = mean_squared_error(y_pred, y_test) 
r_2 = r2_score(y_pred, y_test)

print("Linear MSE values: {}".format(mse))
print("Linear R2 value: {}".format(r_2)) 
print()

arr = np.concatenate((y_train, y_pred))
arr1 = np.concatenate((y_train, y_test))
plt.scatter(df["Year"], arr,color='k') 
plt.scatter(df["Year"], arr1,color='r') 
year_input = df["Year"].values[len(X_train):]
a, b = np.polyfit(year_input, y_pred, 1)
plt.plot(year_input, a*year_input+b)
title = str(a) + "*x " + str(b)
print(title)
plt.title("Prediction Using Linear Model", fontsize = 14)
plt.xlabel("Years")
plt.ylabel("Number of Female MP's")
legend_handles = [
    Patch(color='red', label='Actual Points'),
    Patch(color='black', label='Predicted Points'),
    Patch(color='blue', label='Best-Fit Line'),
    Patch(color='green', label='New Predictions')
]
plt.legend(handles=legend_handles)
prediction_lin = []
for i in prediction_years:
    prediction_lin.append(a*i+b)
plt.scatter(prediction_years, prediction_lin, color = "g")
plt.show()

#################################################################################
#################################################################################
#################################################################################

X_train, X_test, y_train, y_test = train_test_split(feature, label, test_size=6/27, random_state=42, shuffle=False)
poly2 = PolynomialFeatures(degree = 2)

poly2_x_train = poly2.fit_transform(X_train)
reg2 = LinearRegression()
reg2 = reg2.fit(poly2_x_train, y_train)

X_test_poly2 = poly2.fit_transform(X_test)

y_pred_poly2 = reg2.predict(X_test_poly2)

mse2 = mean_squared_error(y_pred_poly2, y_test)
r_22 = r2_score(y_test, y_pred_poly2)

print("Poly2 MSE values: {}".format(mse2))
print("Poly2 R2 value: {}".format(r_22))
print()

arr = np.concatenate((y_train, y_pred_poly2))
arr1 = np.concatenate((y_train, y_test))
plt.scatter(df["Year"], arr,color='k') 
plt.scatter(df["Year"], arr1,color='r') 
year_input = df["Year"].values[len(X_train):]
a, b, c= np.polyfit(year_input, y_pred_poly2, 2)

plt.plot(year_input, a*year_input*year_input + b*year_input + c)
title = str(a) + "*x^2 + " + str(b) + "*x +" + str(c)
print(title)
plt.title("Prediction Using Polynomial Model", fontsize = 14)
plt.xlabel("Years")
plt.ylabel("Number of Female MP's")
plt.legend(handles=legend_handles)

#################################################################################
#################################################################################
#################################################################################

prediction_poly = []
for i in prediction_years:
    prediction_poly.append(round(a*i*i+b*i+c))
print(prediction_poly)
plt.scatter(prediction_years, prediction_poly, color = "g")
plt.show()