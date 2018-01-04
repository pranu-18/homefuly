import numpy as np 

n = np.genfromtxt("data1.tsv", delimiter='\t',dtype=np.int32)
unique_id = [x for x in n if (n == x).sum()==1]
print("ID of missing drone is ",unique_id)