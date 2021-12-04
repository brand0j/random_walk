# random_walk_2-D

You can find all relevant information here https://en.wikipedia.org/wiki/Random_walk

I chose to generate random integers from [1,4] and use that random number in: theta = (random.randint(1,5) * pi/2).
This was to ensure that we were only moving solely in the x-direction or the y-direction.

Using:
      x = x + int(cos(theta))
      y = y + int(sin(theta))
      
theta can only be one of the following values: pi/2 , pi, 3pi/2 , 2pi


x = 0: when y = 1 , -1 ; theta = ( pi/2 , 3pi/2 )
       
y = 0 when x = 1 , -1 ; theta = ( 2pi , pi )
       
As for plotting decisions, it looks much better without a grid layout or spines on the top & right-side.
Clever alpha, linewidth, & markersize values were chosen so you can visibly see areas that were "walked" more than once.
I also plotted the start point (0,0) and the ending point (x(n),y(n)) to help visualize things


I would recommend using n <= 1000 since anything higher than that will computationally take a bit. In the code for n <= 150 it plots the label of each point on the random walk
