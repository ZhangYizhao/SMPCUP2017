
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# In[2]:
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# In[3]:
clf = LogisticRegression(random_state=0, penalty='l2', C=0.1, solver='lbfgs',multi_class='multinomial')
clf.fit(X_train, y_train)

# In[4]:
y_pred = clf.predict(X_test)

# In[5]:
print(accuracy_score(y_test, y_pred))


