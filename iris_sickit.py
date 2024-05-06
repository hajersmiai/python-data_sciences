from json import load
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split as tst , cross_val_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

iris = load_iris()
X_iris=iris.data
y_iris=iris.target
# x_iris,y_iris=load_iris(return_x_y=True)

x_train, x_validate,y_train,y_validate = tst(X_iris, y_iris, test_size = 0.5,random_state=42)

# model = GaussianNB()
model = KNeighborsClassifier(n_neighbors=3) # on sait le nombre d'espèces
model.fit(x_train,y_train)
y_predict=model.predict(x_validate)

print (accuracy_score(y_validate,y_predict))

scores = cross_val_score(model,X_iris, y_iris, cv=10)
print (scores.mean())

model_pca = PCA(n_components=2) # on ne sait pas le nombre d'espèces
model_pca.fit(X_iris, y_iris)
X_2D = model_pca.transform(X_iris)

plt.scatter(X_2D[:,0],X_2D[:,1], c = y_iris, alpha=0.5)
# plt.show()

model_gm = GaussianMixture(n_components=3)
model_gm.fit(X_iris)
y_gm = model_gm.predict(X_iris)
plt.scatter(X_2D[:,0],X_2D[:,1], c = y_gm, alpha=0.6)
plt.show()