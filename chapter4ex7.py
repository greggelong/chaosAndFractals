# time plot 

# importing the required module 
import matplotlib.pyplot as plt 
    
    
def f(x):
    return x*0.5 -2


# lists to hold datat for plots
t = [0]
fx1 =[]
fx2 =[]
fx3 =[]
fx4 =[]
fx5 =[]
#inital seeds
ix1 = 0
ix2 = 1
ix3 = 1.1
ix4 = -4.1
ix5 = -3.9
fx1.append(ix1)
fx2.append(ix2)
fx3.append(ix3)
fx4.append(ix4)
fx5.append(ix5)

for i in range (1,10):
    #send to function
    rx1= f(ix1)
    rx2= f(ix2)
    rx3= f(ix3)
    rx4= f(ix4)
    rx5= f(ix5)
    #append them
    fx1.append(rx1)
    fx2.append(rx2)
    fx3.append(rx3)
    fx4.append(rx4)
    fx5.append(rx5)
    t.append(i)
    #swap
    ix1,ix2,ix3,ix4, ix5= rx1,rx2,rx3,rx4,rx5
    
print(t)
print(fx1)
print(fx2)
print(fx3)
    
# plotting the points  
plt.plot(t, fx1)
plt.plot(t, fx2)
plt.plot(t, fx3)
plt.plot(t, fx4)
plt.plot(t, fx5)
    
# naming the x axis 
plt.xlabel('time - axis') 
# naming the y axis 
plt.ylabel('fx at t - axis') 
    
# giving a title to my graph 
plt.title('feldman') 
    
# function to show the plot
plt.ylim([-5, -2])
plt.show()     
    
    