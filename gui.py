import tkinter as tk
import test
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

if __name__ == '__main__':

    screenName = 'Greensurf'
    window = tk.Tk(screenName)
    networkLabel = tk.Label(text="Network: ")  
    networkLabel.pack()
    networkChartFrame = tk.Frame(background='black', width=800, height=300)
    networkChartFrame.pack()
    networkBtn = tk.Button(master=window, command=test.plot, text='Test')
    networkBtn.pack()

    window.mainloop()