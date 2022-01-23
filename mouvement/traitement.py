import pandas as pd  
import matplotlib.pyplot as plt
data = pd.read_csv("coordonnees1.txt")
data.Y = 400 - data.Y
plt.axis([0, 600, 0, 400])
plt.scatter(data.X,data.Y)
plt.savefig('output.png')