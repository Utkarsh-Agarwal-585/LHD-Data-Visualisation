import matplotlib.pyplot as plt

'''x = [1,4,7,9]
y = [2,45,12,48]

plt.plot(x,y,'r-.')
plt.xlabel("time")
plt.ylabel("distance")
plt.title("my cool graph")
plt.show()'''

x = [i for i in range(10)]
y = [i*i for i in range(10,20)]
z=[i*2 for i in range(10,20)]

plt.subplot(2,1,1) #2 rows ,1 col, 1 currently graph
plt.plot(x,y)

plt.subplot(2,1,2)
plt.plot(x,z)

plt.show()
