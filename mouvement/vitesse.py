import pandas as pd  
import matplotlib.pyplot as plt
data = pd.read_csv("coordonnees11.csv",sep=";")
Dt = 0.5
data["t"] = data["T"] * Dt
data["vx"] = (data.X_suivant - data.X)/Dt
data["vy"] = (data.Y_suivant - data.Y)/Dt
print(data)
plt.scatter(data.t,data.X)
plt.show()