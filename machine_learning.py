import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



rng = np.random.RandomState(42)
x= rng.rand(40)*10
y=2*x-1+rng.randn(40)

model = LinearRegression(fit_intercept=True)
print(x.shape)
X=x[:,np.newaxis]
model.fit(X,y)
print (model.coef_)
print(model.intercept_)
xfit=np.linspace(-1,11,20)
Xfit=xfit[:,np.newaxis]
yfit=model.predict(Xfit)


plt.scatter (x,y)
plt.plot(xfit,yfit,"r-")
plt.show()