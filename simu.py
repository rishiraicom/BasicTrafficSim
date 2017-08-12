# fixed number of cars
cars = [43, 48, 34, 28]
weightTime = [0] * 4
wt = 0
k = 0
st = 10
avgWeighttime = [0] * 4
carsElapsed = [0] * 4
print("hello1")
print(sum(cars))
while sum(cars)!=0:
    k += 1
    print("cycle -----", k)
    print("cars-------",cars)
    #print(randint(2,3))
    print("weight time ----", weightTime)
    if k > 1:
        for l in range(0, 4):
            avgWeighttime[l] = weightTime[l] / carsElapsed[l]
    print("average wait time------", avgWeighttime)
    for i in range(0, 4):
        if cars[i] >= st:
            weightTime[i] = weightTime[i] + (st * wt) + 55
            cars[i] -= st
            carsElapsed[i]+=st
        else:
            weightTime[i] = weightTime[i] + (cars[i] * (cars[i] + 1)) / 2 + cars[i] * wt
            carsElapsed[i] += cars[i]
            cars[i] = 0

        wt += st
        #for j in range(0, 4):
        #    cars[j] = cars[j] + randint(1, 3)

#print(weightTime)

print("hello")
