#Topic:Decision Tree - Class and Regr
#-----------------------------
#Read the case from this link
#https://stackabuse.com/decision-trees-in-python-with-scikit-learn/

#%% Classification Tree - Predict if the Currency is FAKE or not depending upon features

#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
#os.listdir('D:\Training ML Code Notes\Henry Harvin Trainer\PyAnalyticsTrainer\PyAnalyticsTrainerVikas\XIM Later\DT') #change the folder to see what are the file in folder
#dataset
#data = pd.read_csv('E:/analytics/projects/pyanalytics/data/bill_authentication.csv')
data = pd.read_csv('https://raw.githubusercontent.com/DUanalytics/pyAnalytics/master/data/bill_authentication.csv')
data.head()
data.shape
data.columns
#data preparation : X & Y
X= data.drop('Class', axis=1) #axis=1 -> column
y= data['Class']
X
y
y.value_counts()



#split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20)
X_train.shape
X_test.shape


#model
from sklearn.tree import DecisionTreeClassifier
clsModel = DecisionTreeClassifier()  #model with parameter
clsModel.fit(X_train, y_train)

#predict
ypred1 = clsModel.predict(X_test)
ypred1

#metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
cr=classification_report(y_true=y_test, y_pred= ypred1)


confusion_matrix(y_true=y_test, y_pred=ypred1)
accuracy_score(y_true=y_test, y_pred=ypred1)

#new data
newData = X.sample(4)

clsModel.predict(newData)


'''
Gini index or Gini impurity measures the degree or probability of a particular 
variable being wrongly classified when it is randomly chosen. But what is 
actually meant by ‘impurity’? If all the elements belong to a single class, 
then it can be called pure. The degree of Gini index varies between 0 and 1, 
where 0 denotes that all elements belong to a certain class or if there exists 
only one class, and 1 denotes that the elements are randomly distributed across
various classes. A Gini Index of 0.5 denotes equally distributed elements 
into some classes.
'''

#visualise 
#pip install graphviz
from graphviz import Source
from sklearn import tree
tree.plot_tree(decision_tree=clsModel)
tree.plot_tree(decision_tree=clsModel, feature_names=['Var', 'Skew', ' Kur',  'Ent'], class_names=['Orgiginal','Fake'], fontsize=8)
#not a good way to draw graphs.. other methods to be experimented
tree.plot_tree(decision_tree=clsModel, max_depth=2, feature_names=['Var', 'Skew', ' Kur',  'Ent'], class_names=['Orgiginal','Fake'], fontsize=8)
tree.plot_tree(decision_tree=clsModel, max_depth=3, feature_names=['Var', 'Skew', ' Kur',  'Ent'], class_names=['Orgiginal','Fake'], fontsize=8)
