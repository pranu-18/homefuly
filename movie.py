import numpy as np 

def check(movie_time_list, train_journey):
    store = {}
    for i, time in enumerate(movie_time_list):
        if train_journey - time in store:
	        return True
        store[time] = i
    return False

a = np.genfromtxt("data2.tsv",dtype=np.int32)
train_journey = input("Enter your travel length in minutes : ")
if(check(a,int(train_journey))):
	print("You can watch two movies")
else:
	print("Sorry! You cannot watch two movies")


