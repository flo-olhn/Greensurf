import numpy as np
import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def networkTrafficEmissions():
    values = psutil.net_io_counters()
    bytes_sent = values[0]
    bytes_received = values[1]
    total_bytes = bytes_sent + bytes_received
    total = (total_bytes * 1.52E-10) * 0.057
    return total

def animate(i):
    time_axis.append(i)
    total.append(round(networkTrafficEmissions(), 10))
    avg =  [np.mean(total)] * len(total)
    plt.cla()
    plt.ylabel("GHG Emission - kgCO2eq")
    plt.xticks([])
    plt.yscale("log")
    plt.plot(time_axis, total, color='#46DB96', linewidth=0.5)
    plt.fill_between(time_axis, total, color='#46DB96', alpha=0.2)
    plt.plot(time_axis, avg, color='blue', linewidth=0.5, alpha=0.4, ls='--', )
    # Uncomment the line below to display average GHG Emission value on chart
    #plt.annotate(str(avg[0]), xy=(avg[0], avg[0]))

if __name__ == '__main__':
    time_axis = []
    total = []
    ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    plt.show()
