import random
import numpy as np
import matplotlib.pyplot as plt

def random_walk(n):
    x,y=0,0
    for i in range(n):
        (dx,dy)=random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x+=dx
        y+=dy
    return (x,y)



how_many_simulations=10000
step_num=1000
far_counter=0
step_max=50

x_list=[]
y_list=[]
 
for i in range(how_many_simulations):
    x,y=random_walk(step_num)
    x_list.append(int(x))
    y_list.append(int(y))
    distance=abs(x)+abs(y)
    if distance >= step_max:
        far_counter += 1

print(far_counter/how_many_simulations)

plt.scatter(x_list,y_list,alpha=0.1,s=30)

plt.show()