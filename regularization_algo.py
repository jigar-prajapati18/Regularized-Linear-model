

#Ridge regression

import numpy as np
import matplotlib.pyplot as plt
m=100
x=6*np.random.rand(m,1)-3
y=0.5*x**2+x+2+np.random.rand(m,1)

from sklearn.linear_model import Ridge

ridge_reg=Ridge(alpha=1,solver="cholesky")
ridge_reg.fit(x,y)
pred=ridge_reg.predict([[1.5]])
#print(pred)

#using stochastic GD

from sklearn.linear_model import SGDRegressor
sgd_reg=SGDRegressor(penalty="l2")
sgd_reg.fit(x,y.ravel())
y_pred=sgd_reg.predict([[1.5]])
print(ypred)
print(sgd_reg.intercept_)
print(sgd_reg.coef_)

# Lassp reg
from sklearn.linear_model import Lasso
lasso_reg=Lasso(alpha=0.1)
lasso_reg.fit(x,y)
y_pred=lasso_reg.predict([[1.5]])
print(ypred)
print(lasso_reg.intercept_)
print(lasso_reg.coef_)

#Elastic Net

from sklearn.linear_model import ElasticNet

Elastic_reg=ElasticNet(alpha=0.1,ratio=0.5)
Elastic_reg.fit(x,y)
y_pred=Elastic_reg.predict([[1.5]])
print(ypred)
print(Elastic_reg.intercept_)
print(Elastic_reg.coef_)









