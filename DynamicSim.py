from random import randint

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
# print(sum(cars))
while k < 50:
    k += 1
    print("cycle ------------", k - 1)
    # print("cars-------", cars)
    # print(randint(2,3))
    print("cars elapsed--------------", carsElapsed)
    #print("weight time ------", weightTime)
    print("Cars in lane1-------------", len(lane1))
    print("Cars in lane2-------------", len(lane2))
    print("Cars in lane3-------------", len(lane3))
    print("Cars in lane4-------------", len(lane4))
    lenofLane1 += len(lane1)
    #print("average length of lane1---", lenofLane1 / k)
    if k > 1:
        for l in range(0, 4):
            avgWeighttime[l] = weightTime[l] / carsElapsed[l]
            #avgofavgTime[l] += avgWeighttime[l]
            #print("avg of avg ", avgofavgTime[l] / k)
    print("average wait time per Car-", avgWeighttime)
    for i in range(0, 4):
        # will calculate st here
        for j in range(0, st):
            if AllLane[i]:
                rm = AllLane[i].pop()
            carsElapsed[i] += 1
            weightTime[i] += rm + j

        for ls in AllLane:
            for g in range(0, len(ls)):
                ls[g] += st

        for ls in AllLane:
            randomNum0 = randint(4, 6)
            for _ in range(0, randomNum0):
                ls.insert(0, 0)

