import numpy as np
from collections import Counter

############################################################################
# DO NOT MODIFY CODES ABOVE 
############################################################################

class KNN:
    def __init__(self, k, distance_function):
        """
        :param k: int
        :param distance_function
        """
        self.k = k
        self.distance_function = distance_function
        #self.features=[]
        #self.labels=[]

    # TODO: save features and lable to self
    def train(self, features, labels):
        """
        In this function, features is simply training data which is a 2D list with float values.
        For example, if the data looks like the following: Student 1 with features age 25, grade 3.8 and labeled as 0,
        Student 2 with features age 22, grade 3.0 and labeled as 1, then the feature data would be
        [ [25.0, 3.8], [22.0,3.0] ] and the corresponding label would be [0,1]

        For KNN, the training process is just loading of training data. Thus, all you need to do in this function
        is create some local variable in KNN class to store this data so you can use the data in later process.
        :param features: List[List[float]]
        :param labels: List[int]
        """
        #raise NotImplementedError
        self.features=features
        self.labels=labels

    # TODO: find KNN of one point
    def get_k_neighbors(self, point):
        """
        This function takes one single data point and finds k-nearest neighbours in the training set.
        You already have your k value, distance function and you just stored all training data in KNN class with the
        train function. This function needs to return a list of labels of all k neighbours.
        :param point: List[float]
        :return:  List[int]
        """
        #raise NotImplementedError
        c=[]
        distance=[]
        for i in range(len(self.labels)):
            distance.append([self.distance_function(self.features[i],point),i])
        distance.sort(key=lambda x:(x[0],x[1]))
        if self.k < 1:
            return c
        for i in range(self.k):
            c.append(self.labels[distance[i][1]])
        return c
		
	# TODO: predict labels of a list of points
    def predict(self, features):
        """
        This function takes 2D list of test data points, similar to those from train function. Here, you need to process
        every test data point, reuse the get_k_neighbours function to find the nearest k neighbours for each test
        data point, find the majority of labels for these neighbours as the predicted label for that testing data point (you can assume that k is always a odd number).
        Thus, you will get N predicted label for N test data point.
        This function needs to return a list of predicted labels for all test data points.
        :param features: List[List[float]]
        :return: List[int]
        """
        #raise NotImplementedError	
        res=[]
        for point in features:
            diction={}
            c=np.array(self.get_k_neighbors(point))
            maxi=0
            #lab=c[0]

            for label in c:
                if label not in diction.keys():
                    diction[label]=1
                else:
                    diction[label]+=1
                if diction[label]>maxi:
                    maxi=diction[label]
                    lab=label
            res.append(lab)
        return res
    

if __name__ == '__main__':
    print(np.__version__)
