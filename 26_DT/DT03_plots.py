#Topic:Visualising Decision Tree in Python
#-----------------------------
#libraries

#4 ways
# sklearn.tree.export_text
# sklearn.tree.plot_tree (matplot needed)
# skearn.tree.export_graphviz  (graphviz needed)
# dtreeviz package (dtreeviz and graphvis needed)


import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

iris = datasets.load_iris()
X = iris.data
y = iris.target
iris.feature_names

clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(X,y)


#plottree
tree.plot_tree(decision_tree=clf, fontsize=8)

fig = plt.figure(figsize=(10,8))
_ = tree.plot_tree(clf, filled=True, fontsize=7)  #see plot

import graphviz
dot_data = tree.export_graphviz(decision_tree=clf, out_file=None, feature_names = iris.feature_names, class_names = iris.target_names, filled=True)
graph = graphviz.Source(dot_data, format='png')
#error dot path
