from scipy.optimize import linprog
import numpy as np

values=[]
weights=[]
with open('./data/ks_4_0','r') as f:
        item_count,capacity = map(int,f.readline().split())
        for line in f:
            v,w = line.split()
            values.append(-int(v))
            weights.append(int(w))

result = linprog(c=np.array(values),A_ub=np.array([weights]),b_ub=capacity,A_eq=np.eye(item_count),b_eq=np.ones(item_count))

print(result)
