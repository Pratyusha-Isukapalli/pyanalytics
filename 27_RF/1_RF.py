'''
You are right that the two concepts are similar. As is implied by the names 
"Tree" and "Forest," a Random Forest is essentially a collection of Decision 
Trees. A decision tree is built on an entire dataset, using all the features
/variables of interest, whereas a random forest randomly selects observations
/rows and specific features/variables to build multiple decision trees from 
and then averages the results. After a large number of trees are built using 
this method, each tree "votes" or chooses the class, and the class receiving 
the most votes by a simple majority is the "winner" or predicted class.

When using a decision tree model on a given training dataset the accuracy
 keeps improving with more and more splits. You can easily overfit the data
 and doesn't know when you have crossed the line unless you are using cross
 validation (on training data set). The advantage of a simple decision tree 
 is model is easy to interpret, you know what variable and what value of that
 variable is used to split the data and predict outcome.

A random forest is like a black box and works as mentioned in above answer.
 It's a forest you can build and control. You can specify the number of trees
 you want in your forest(n_estimators) and also you can specify max num of
 features to be used in each tree. But you cannot control the randomness, you 
 cannot control which feature is part of which tree in the forest, you cannot 
 control which data point is part of which tree. Accuracy keeps increasing 
 as you increase the number of trees, but becomes constant at certain point. 
 Unlike decision tree, it won't create highly biased model and reduces the 
 variance.

When to use to decision tree:

    When you want your model to be simple and explainable
    When you don't want to worry about feature selection or regularization or
    worry about multi-collinearity.
    You can overfit the tree and build a model if you are sure of validation 
    or test data set is going to be subset of training data set or almost
    overlapping instead of unexpected.

When to use random forest :

    When you don't bother much about interpreting the model but want better 
    accuracy.
    Random forest will reduce variance part of error rather than bias part,
    so on a given training data set decision tree may be more accurate than
    a random forest. But on an unexpected validation data set, Random forest 
    always wins in terms of accuracy.
'''

'''
The success of a random forest highly depends on using uncorrelated decision 
trees. If we use same or very similar trees, overall result will not be much 
different than the result of a single decision tree. Random forests achieve 
to have uncorrelated decision trees by bootstrapping and feature randomness.
'''

#Random Forests - iris
#https://github.com/alexhwoods/Machine-Learning/tree/master/Random%20Forest
# RandomForests
# First let's import the dataset, using Pandas.
import numpy as np
import pandas as pd

train = pd.read_csv("train-iris.csv")    # make sure you're in the right directory if using iPython!
test = pd.read_csv("test-iris.csv") 

train.head()             # ignore the first column, it's how I split the data.
train.describe(include='all')
train.columns
train.petal_length.describe()   #class not working because of keyword
train.describe(include=[np.object])
#train.describe(include=['category'])  #nothing so far
train.describe(exclude=[np.number])
train['class'].value_counts()
test['class'].value_counts()

from sklearn.ensemble import RandomForestClassifier


#%%# however, are data has to be in a numpy array in order for the random forest algorithm to except it!
cols = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width']
colsRes = ['class']


trainArr = train[cols].values    # training array
#trainArr = train.as_matrix(cols)    # training array
trainArr
trainRes = train[colsRes].values
(colsRes) # training results
trainRes
## Training!

rf = RandomForestClassifier(n_estimators=100)    # 100 decision trees is a good enough number
rf.fit(trainArr, trainRes)          # finally, we fit the data to the algorithm!!! :)

# note - you might get an warning saying you entered a 2 column vector..ignore it.

#%%
## Testing!

# put the test results in the same format!
testArr = test[cols].values
results = rf.predict(testArr)

# add it back to the dataframe, so I can compare side-by-side
test['predictions'] = results
test.head()

