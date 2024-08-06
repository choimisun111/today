import matplotlib.pyplot as plt

x = [17,18,19,20,21,22,23]
y = [65,70,70,75,80,85,85]

plt.plot(x ,y, marker = "x", linestyle="-",color="red",label="humidity")
plt.title("dDaily humidity")
plt.xlabel("Time ( Hour)")
plt.ylabel("humidity (%)")
plt.legend()
plt.grid(True)
# plt.show()
plt.savefig("./linechart.png")