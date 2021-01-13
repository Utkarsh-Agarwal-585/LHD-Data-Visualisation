import matplotlib.pyplot as plt 
import numpy as np

hours=[2,6,1,4,2,6,2,1]
activity=["ready","college","rest","study","play","sleep","tv","yoga"]
explodes= [0.2,0,0,0,0,0,0,0]
plt.pie(hours, labels=activity,shadow=True,explode= explodes)
plt.show()