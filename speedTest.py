from time import *
import random as r 

def mistake(para,user):
    error = 0
    for i in range(len(para)):
        try:
            if para[i] != user[i]:
                error += 1
        except:
            error += 1
    return error

def timeDelay(start,end,user):
    time_delay = end - start
    time_Rdelay = round(time_delay,2)
    speed = len(user)/time_Rdelay

    return round(speed)

test = ["My name is anirudh","i live i kalyan","I study in Ruia College"]
test1 = r.choice(test)
print(" ***************typing Speed***************")
print()
print(test1)
print()
print()
time_1 = time()
testInput = input()
time_2 = time()
print("Speed : ", timeDelay(time_1,time_2,testInput), "w/sec")

print("\nMistakes made: ",mistake(test1,testInput))
