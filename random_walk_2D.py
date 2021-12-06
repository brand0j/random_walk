## IMPORT ##
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
import pandas as pd
import seaborn as sns 

# A random walk with n number of steps 
n=750

# Starts at (0,0), initialize for replacement
x=np.zeros(n+1) 
y=np.zeros(n+1)


# Set up our plot (plt.grid() makes this hard to see

fig = plt.figure(figsize=(10,10))
ax=fig.add_subplot(1,1,1)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Random Walk 2-D: "+str(n)+" steps")
plt.grid(alpha=0.15)

    
# Generate a random n*pi/2 value where n is a random integer
# This makes it so either we move in the x-direction OR the y-direction, but not both

for i in range(1,n+1):
    
    # x,y values
    theta = (np.random.randint(1,5)*np.pi)/2
    x[i] = x[i-1]+ int(np.cos(theta))
    y[i] = y[i-1]+ int(np.sin(theta))

        
    # Need this to draw the lines from point to point
    x_values = [x[i-1],x[i]]
    y_values = [y[i-1],y[i]]

        
    # Styling the lines. -- dash with markers for the points. 
    # Set alpha <1 so we can visualize paths that are taken more than once


    plt.plot(x_values,y_values,color="#4CB391",
        linestyle='--',alpha=0.4,linewidth=0.6,
        marker='o',markerfacecolor="#4CB391",markersize=0.45)


#Makes the graph a little nicer to look at#
ax.set_xlim(min(x)-5,max(x)+5)
ax.set_ylim(min(y)-5,max(y)+5)


#Seaborn plot & data frame with pandas#
coord = list(zip(x,y))
df = pd.DataFrame(coord,columns=['X','Y'])
sns.jointplot(x='X',y='Y',data=df,
    kind="hex",
    color="#4CB391",
    gridsize=20)
sns.set_theme(style="ticks")
plt.grid(alpha=0.2)


plt.show()