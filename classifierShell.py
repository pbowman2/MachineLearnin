import numpy as np
from sklearn.model_selection import train_test_split
class HardcodedClassifier:
    def __init__(self):
        from sklearn import datasets
        self.iris = datasets.load_iris()
    def createLearnTestSets(self):
        self.dataTrain, self.dataTest, self.targetTrain,self.targetTest = (
            train_test_split(self.iris.data, self.iris.target, 
                             test_size=.30)) 

    def train(self):
        print "Yeah sure I'll get right on that...."
    def predict(self):
        return 0
    def tests(self):
        correct = 0
        for item in self.targetTest:
            if item == self.predict():
                correct +=1.
        accuracy = (correct / self.targetTest.size) * 100
        print('We guessed with a %2.1f%% accuracy' % accuracy) 
            
test = HardcodedClassifier()
test.createLearnTestSets()
test.train()
test.tests()
