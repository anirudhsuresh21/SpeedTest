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

test = ["On a sunny day, I enjoy taking long walks in the park with my friendly and energetic dog, Max.",
        "The sun is bright and the sky is blue.",
        "She walked to the store, bought some groceries, and then caught the bus home.",
       "The cat chased the mouse."]
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
