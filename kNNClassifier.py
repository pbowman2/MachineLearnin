import numpy as np
class KNNClassifier:
    def __init__(self):
       )
    def createLearnTestSets(self):
        self.dataTrain, self.dataTest, self.targetTrain,self.targetTest = (
            train_test_split(self.iris.data, self.iris.target, 
                             test_size=.30)) 

    def train(self, data):
        self.data = data
    def predict(self):
        return 0
    def tests(self):
        correct = 0
        for item in self.targetTest:
            if item == self.predict():
                correct +=1.
        accuracy = (correct / self.targetTest.size) * 100
        print('We guessed with a %2.1f%% accuracy' % accuracy) 
            
from sklearn import datasets
iris = datasets.load_iris()
test = KNNClassifier()
test.createLearnTestSets()
test.train(iris)
test.tests()
