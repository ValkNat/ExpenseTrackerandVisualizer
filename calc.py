#imports
import requests
import numpy as np
import matplotlib.pyplot as plt
import pandas as panda
import tkinter as tk
from tkinter import *

#tkinter setup + initialization
t = Tk()
t.geometry("700x700")
t.title("Stock Visualizer")


def Parse():
    symbol = enter_symbol.get()
    #pulling and parsing data from AlphaVantage API
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=0IUTAP2M1MBDCBOX'
    r = requests.get(url)
    data = r.json()
    time_series = data["Time Series (5min)"]

    #defining arrays in numpy
    opens = np.array([float(entry["1. open"]) for entry in time_series.values()])
    timestamps = np.array(list(time_series.keys()), dtype=np.datetime64)

    return symbol, opens, timestamps

#matplotlib visualization and data parsing
def Visualize():
    
    symbol, opens, timestamps = Parse()

    #data visualization with matplotlib
    plt.plot(opens, timestamps)
    plt.xlabel("Time")
    plt.ylabel("Opens")
    plt.title(f"Open Time Series: {symbol}")
    plt.show()

#pandas dataframe (makes data savable to CSV)
def CSVSave():
    timestamps, opens = Parse()
    dataframe = panda.DataFrame(timestamps, opens)
    dataframe.to_csv('data.csv', sep='\t')

#tkinter widget setup
enter_symbol = tk.Entry()
enter_symbol.pack()
visualize_data = tk.Button(text = "Visualize Data", command=Visualize)
visualize_data.pack()
save_to_csv = tk.Button(text = "Save Data", command=CSVSave)
save_to_csv.pack()

#runs tkinter window
t.mainloop()

