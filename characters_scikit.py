from sklearn.datasets import load_digits
from sklearn.manifold import Isomap
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import make_blobs
import numpy as np


fig, axes = plt.subplots(10,10,figsize = (8,8),subplot_kw={"xticks":[], "yticks": []},
                        gridspec_kw={"hspace":0.1, "wspace":0.1})

digits = load_digits()

for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i],cmap="binary")
    ax.text(0.05,0.05,str(digits.target[i]), transform=ax.transAxes, color="green")

# fig.show()
x= digits.data
y= digits.target

model_iso = Isomap(n_components=2)
model_iso.fit(x)
x_iso=model_iso.transform(x)



# plt.figure()
# plt.scatter(x_iso[:,0],x_iso[:,1],c=y, cmap=plt.cm.get_cmap("Spectral",10))
# plt.colorbar(ticks=range(10))
# plt.show()

model=GaussianNB()
x_train, y_train, x_validate,y_validate= train_test_split(x,y)
model.fit(x_train,y_train)
y_predict = model.predict(x_validate)
score = accuracy_score(y_validate,y_predict)
print (score)
confusion = confusion_matrix(y_validate, y_predict)
print(confusion)

input()
