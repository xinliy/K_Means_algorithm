import numpy as np
import matplotlib.pyplot as plt

#a dataSet to train
dataSet=np.array([[1,2],
                  [2,3],
                  [7,8],
                  [8,10],
                  [11,12],
                  [-1,-1],
                  [4,7],
                  [10,10],])


class K_Means:
    def __init__(self,center_number=2,tolerance_value=0.001,iteration_time=300):
        self.center_number=center_number
        self.tolerance_value=tolerance_value
        self.iteration_time=iteration_time

    #To realize the K_Means algorithm
    def fit(self,dataSet):
        self.center_dictionary={}
        # Get the origin center points
        for i in range(self.center_number):
            self.center_dictionary[i] = dataSet[i]


        #Max iterate time
        for i in range(self.iteration_time):
            print(i)
            print(self.center_dictionary)

            #To record which point belongs to which center
            ownership_dictionary = {}
            for every_center in range(self.center_number):
                ownership_dictionary[every_center] = []

            #Iterate every point
            for point_index in range(len(dataSet)):
                distance_list=[]
                for every_center in range(self.center_number):
                    #Get the distance to every center point
                    distance_list.append(np.linalg.norm(dataSet[point_index]-self.center_dictionary[every_center]))
                idx=distance_list.index(min(distance_list))
                for every_center in range(self.center_number):

                    if idx==every_center and point_index not in ownership_dictionary[every_center]:
                        ownership_dictionary[every_center].append(point_index)

            right_center_point=0
            print(ownership_dictionary)
            for every_center in range(self.center_number):
                new_center=np.asarray([0,0])
                for every_point in ownership_dictionary[every_center]:
                    new_center+=dataSet[every_point]
                new_center=new_center/len(ownership_dictionary[every_center])
                j = 0
                for i in range(len(dataSet[0])):
                    if float(self.center_dictionary[every_center][i])==float(new_center[i]):
                        j+=1
                    if j==len(dataSet[0]):
                        right_center_point+=1
                if right_center_point==self.center_number:
                    return 0
                self.center_dictionary[every_center]=new_center


    def predict(self,dataSet):
        pass


clf=K_Means()
clf.fit(dataSet)
print('My own center: ',clf.center_dictionary)


from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=2).fit(dataSet)
print('True center: ',kmeans.cluster_centers_)
print('labels:',kmeans.labels_)

for i in range(len(dataSet)):
    plt.scatter(dataSet[i][0],dataSet[i][1],s=30,c='b')

for i in range(clf.center_number):
    colors=['y','m','c','r']
    plt.scatter(clf.center_dictionary[i][0],clf.center_dictionary[i][1],s=40,c=colors[i],marker='*')



plt.show()