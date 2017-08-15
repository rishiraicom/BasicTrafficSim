from random import randint
import pickle
from sklearn import svm
import os

'''
class Cars:
    def __init__(self, rnumber, pos):
        self.roundNo = rnumber
        self.position = pos

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
'''

# loading saved trained svm model
classifier_filename = os.path.expanduser("E:\college\project traffic\SavedModels\SVMmodel.sav")
SVMmodel = pickle.load(open(classifier_filename, 'rb'))


# print("Example predict ----",SVMmodel.predict([[.4, .8, 1]]))

# function to calculate dynamic st(i should have chosen other variable name) value
def calst(X, num):
    t = []
    for k in range(0, 3):
        t.append(X[(num + k) % 4])
    maxnum = max(t)
    # print("t before---------", t)
    for loopv in range(0, 3):
        t[loopv] = t[loopv] / maxnum
    # print("t after---------", t)
    temp = SVMmodel.predict([t])
    # print("prediction catigory--------",temp)
    if temp[0] == '1':
        stemp = 25
    elif temp[0] == '2':
        stemp = 22
    elif temp[0] == '3':
        stemp = 18
    else:
        stemp = 15
    if t[0] == t[1] and t[1] == t[2]:
        stemp = 20
    if stemp < X[num]:
        return stemp
    else:
        temp1 = X[num]
        return temp1


lane1 = [0] * 25
lane2 = [0] * 25
lane3 = [0] * 25
lane4 = [0] * 25
AllLane = []
AllLane.append(lane1)
AllLane.append(lane2)
AllLane.append(lane3)
AllLane.append(lane4)

avgofavgTime = [0] * 4
weightTime = [0] * 4
lenofLane1 = 0
wt = 0
k = 0
st = 20
avgWeighttime = [0] * 4
carsElapsed = [0] * 4
print("hello1")
TrafficType = input("Stataic(s) or Dynamic(d)?")
# print(sum(cars))

# main loop
while k < 50:
    k += 1
    print("---------------------------------------------------------")
    print("")
    print("")
    print("------------------After cycle", k - 1, "---------------------")
    # print("cars-------", cars)
    # print(randint(2,3))
    print("cars elapsed--------------", carsElapsed)
    # print("weight time ------", weightTime)
    print("Cars in lane1-------------", len(lane1))
    print("Cars in lane2-------------", len(lane2))
    print("Cars in lane3-------------", len(lane3))
    print("Cars in lane4-------------", len(lane4))
    lenofLane1 += len(lane1)
    # print("average length of lane1---", lenofLane1 / k)
    combinedWeight = 0
    combinedElpsed = 0
    if k > 1:
        for l in range(0, 4):
            avgWeighttime[l] = weightTime[l] / carsElapsed[l]
            # avgofavgTime[l] += avgWeighttime[l]
            # print("avg of avg ", avgofavgTime[l] / k)
            combinedWeight += weightTime[l]
            combinedElpsed += carsElapsed[l]
        print("combined weight time------", combinedWeight / combinedElpsed)
    print("average wait time per Car-", avgWeighttime)

    # loop for each lane
    for i in range(0, 4):

        # st(Static Time) is calculated here
        listOfCars = [len(x) for x in AllLane]
        if TrafficType == "d" and k > 1:
            st = calst(listOfCars, i)
        # print("st-------",st)
        for j in range(0, st):
            if AllLane[i]:
                rm = AllLane[i].pop()  # removing car from lane
            carsElapsed[i] += 1
            weightTime[i] += rm  # adding the weighting time of elapsed cars

        # adding weight time = st in all the cars still in lane
        for ls in AllLane:
            for g in range(0, len(ls)):
                ls[g] += st
        # adding cars in each lane
        for ls in AllLane:
            randomNum0 = randint(4, 5)
            for _ in range(0, randomNum0):
                ls.insert(0, st/randomNum0)
