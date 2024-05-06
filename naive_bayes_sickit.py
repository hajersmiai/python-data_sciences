from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
import numpy as np

X,y=make_blobs(100,2,centers=2,random_state=2,cluster_std=1.5)
model=GaussianNB()
model.fit(X,y)
rng = np.random.RandomState(0)
Xnew =[-6,-14]+[14,18]*rng.rand(2000,2)
ynew = model.predict(Xnew)

plt.scatter(X[:,0],X[:,1],c=y,cmap="RdBu",s=50)
plt.scatter(Xnew[:,0],Xnew[:,1],c=ynew, s=50, alpha=0.1)
plt.show()