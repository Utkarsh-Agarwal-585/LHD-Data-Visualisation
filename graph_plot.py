import matplotlib.pyplot as plt 
import numpy as np

'''x=np.arange(-10,10,0.1)
#y = np.sin(x)
y = x*x + 2*x + 5
plt.plot(x,y)
plt.show()'''

#plt.bar(x,y,width,color)

x=[i for i in range(10)]
y=[4,1,7,2,9,0,12,5,6,8]
x2=[i+0.2 for i in range(10)]
z=[4,2,9,2,4,0,1,5,5,2]
plt.bar(x,y,color="blue",width=0.2,label="2017")
plt.bar(x2,z,color="red",width=0.2,label="2018")
plt.legend()
plt.show()
