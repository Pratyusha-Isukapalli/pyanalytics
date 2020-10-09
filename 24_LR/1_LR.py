#Topic:Linear Model - Steps
#-----------------------------
#libraries

#S1- libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#S2 - data
x = np.array([5,15,25,35,45,55]).reshape((-1,1))  #making 2 dim
x  #IV
y = np.array([5,20,14,32,22, 38])  #1 dim
y #DV #(y can 2 dim also : y.reshape((-1,1)))

plt.scatter(x,y)



#S3 - Model
model = LinearRegression()  #create blank model
#other options- fit_intercept (y/N), normalise i/p var
model.fit(x,y)  #find optimal values of weights b0, b1 using x & y, .fit() fits the model

#model = LinearRegression().fit(x,y) #another way  #2 lines into 1

#S4 - Results
r_sq = model.score(x, y)
r_sq

#S5 Predict
y_pred = model.predict(x)  #predict on trained data 
y_pred


x_pred=np.array([65,70,75]).reshape((-1,1))
y_pred1 = model.predict(x_pred)  #predict on trained data 
y_pred1



plt.scatter(x,y)
plt.scatter(x, y_pred)
plt.scatter(x_pred, y_pred1)





#new values
x_new = np.arange(5).reshape((-1,1))
x_new
y_new = model.predict(x_new)
print(y_new, sep ='\t ')


#%% MUltiple Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression
x = [[0,1], [5,1], [15,2], [25,2], [35,11], [45,15], [55,34], [60,35]]
x
y = [4,5,20,14,32,22,38,43]
y
x, y = np.array(x), np.array(y)
x #2 dim ; MLR - 2 variable, 2 dim(LxB) with 2 columns
y #1 dim
x.shape, y.shape

#S3: Model & Fit
model = LinearRegression().fit(x,y)
model.score(x,y)  #R2 
model.intercept_ # constant
model.coef_ #b0, b1
#keeping one IV constant(x1), if x2 increases by 1 unit, y increases by .28 units and so on

#S4 : predict
y_pred = model.predict(x)
y_pred
y_pred2 = model.intercept_ + np.sum(model.coef_ * x, axis=1)
y_pred2
y_pred - y_pred2

#new data
x_new = np.arange(10). reshape((-1,2))
x_new
y_new = model.predict(x_new)
y_new


