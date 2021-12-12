# This is a script to conduct a multivariate linear regression on housing prices
# using gradient descent based on various inputs. Similar to lesson by Euan Russano. 

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\danma\Documents\Python Scripts\Housingprices.csv')
# See if any data is missing
#print(pd.isna(df).any())
# Get values, and make "Neighborhood" location numeric in the dataset
# 0 = North, 1 = East, 3 = West. South isn't included, but we can make some assumptions
# by assuming the data set is a continuous distribution (ex 1.5 = South East)
x = df[['SqFt','Bedrooms','Bathrooms','Neighborhood']].values
y = df['Price'].values.reshape(-1,1)

#plot inputs to see inital relationships
#fig,axs = plt.subplots(2,2)
#axs[0,0].plot(x[:,0],y,'o')
#axs[0,1].plot(x[:,1],y,'x')
#axs[1,0].plot(x[:,2],y,'*')
#axs[1,1].plot(x[:,3],y,'d')

# We can use adjusted R^2, or a PCA to assess which are the most
# important variables. However, lets check first what the 
# correlation coefficients looks like for linearity.
# We realistically should also be checking for homogeneity in variance (assumed for now), and 
# building our model with a test set (80% of data typically) to be used on a validation set (remaining 20% of data).
# However, we will ignore both for this small test case.

P1 = np.corrcoef(x, y, rowvar = False)[0,:]
# P1 = [1., 0.48380711, 0.5227453 , 0.30131805, 0.55298224])
# Not the strongest single correlation values, but we can optimize based on 
# all the inpjuts none the less.

# Add a column of ones as a reference scaling factor for normalization.
X = np.concatenate((np.ones((len(x),1)),x),axis=1)

# Normalize the data to prep for a multivariate ordinary least squares regression.
Xnorm = X.copy()
xmin = np.min(X[:,1:])
xmax = np.max(X[:,1:])  
Xnorm[:,1:] = (X[:,1:]-xmin)/(xmax-xmin)

ynorm = y.copy()
ymax = np.max(y)
ymin = np.min(y)
ynorm = (y-ymin)/(ymax-ymin)
sortidx = np.argsort(ynorm[:,0])# Sort our normalized housing prices

theta0 = np.zeros((X.shape[1],1))+0.4 # initial coefficient estimates for regression
ypred = Xnorm.dot(theta0) # predicted prices form the initial guess

# Plot the sorted 'actual' prices and the 'predicted' prices.
# =============================================================================
# plt.plot(ynorm[sortidx,0],'o')
# plt.plot(ypred[sortidx,0],'--')
# =============================================================================

# Now lets define our optimization functions
# The cost function is the sum of squared residuals for the predicted fit vs. the actual data. This is a value we wish to minimuze in our case.
def cost(theta):
    J = np.sum((Xnorm.dot(theta)-ynorm)**2,axis=0)[0]
    return J

# 'grad' defines the derivative of the sum of squared residuals of cost. 
# We want this derivative to be as close to zero as possible to indicate we've reached a local minima.
def grad(theta):
    m = len(ynorm)
    dJ = 1/m*np.sum((Xnorm.dot(theta)-ynorm)*Xnorm,axis=0).reshape(-1,1)
    return dJ

# 'GD' is our gradient descent algorithm to minimize the value of the cost function.
# To start we will specify a learning rate of 0.08, 2000 iterations, 
# and a tolerance to terminate at 1e-7.
def GD(theta0, learning_rate = 0.08, epochs = 2000, TOL = 1e-7):
    theta_history = [theta0]
    J_history = [cost(theta0)]
    
    print(f'epoch \t Cost(J) \t')
    for epoch in range(epochs):
        if epoch%25 == 0:
            print(f'{epoch:5d}\t{J_history[-1]:7.4f}\t')
        dJ = grad(theta0)
        J = cost(theta0)
            
        thetanew = theta0 - learning_rate*dJ
        theta_history.append(thetanew)
        J_history.append(J)
        
        if np.sum((thetanew - theta0)**2) < TOL:
               print('Convergence Achieved on iteration: ' + str(epoch))
               print('Tolerance at Convergence: ' + str(np.sum((thetanew - theta0)**2)))
               break 
        theta0 = thetanew
    return thetanew,theta_history,J_history

#Now we call our optimization algorithm, and get our prediction function 
# coefficients!

theta,theta_history,J_history = GD(theta0)
# Plot J_history to see how the residuals dropped with each iteration
#plt.plot(J_history)  

#Now lets get our predicted function output and un-normalize.
# Plot to see what our regression looks like over the original data set.
yprednorm = Xnorm.dot(theta)
ypred = yprednorm*(ymax-ymin) + ymin


fig,axs = plt.subplots(2,2)
axs[0,0].plot(x[:,0],y,'o')
axs[0,0].plot(x[:,0],ypred,'o')
axs[0,1].plot(x[:,1],y,'x')
axs[0,1].plot(x[:,1],ypred,'x')
axs[1,0].plot(x[:,2],y,'*')
axs[1,0].plot(x[:,2],ypred,'*')
axs[1,1].plot(x[:,3],y,'d')
axs[1,1].plot(x[:,3],ypred,'d')

# To show some statistical signifigance in the fit, we should prove that the 
# 95% confidence interval for each coefficient determined doesn't include 0. 
# This is easily facilitated with a library like scikit-learn if necessary.
