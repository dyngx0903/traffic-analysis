import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def sum(array):
  result = 0
  for i in range(0,len(array)):
    result += array[0]
  return result

def getTraffic(date, destination):
    filename = f"vehicles_{date}.txt"
    filepath = os.path.join("traffic", filename)

    # Define the number of time intervals (6:00 AM to 9:00 PM)
    time_intervals = 15  # 6 AM to 9 PM inclusive
    cars = [0] * time_intervals
    giants = [0] * time_intervals
    motors = [0] * time_intervals

    try:
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.split(':')
                if len(parts) != 2:
                    continue

                meta, traffic_data = parts
                loc, timestamp = meta.split('-')[:2]  # Extract location and timestamp
                if destination != "all" and loc != destination:
                    continue

                # Extract hour index from the timestamp
                time_parts = timestamp.split('_')
                hour = int(time_parts[3])
                if 6 <= hour < 21:  # Adjusted time range: 6:00 AM to 9:00 PM
                    index = hour - 6
                else:
                    continue

                # Parse the traffic data
                for entry in traffic_data.split(','):
                    entry = entry.strip()
                    if "car" in entry:
                        cars[index] += int(entry.split()[1])
                    elif "truck" in entry or "bus" in entry:
                        giants[index] += int(entry.split()[1])
                    elif "motor" in entry:
                        motors[index] += int(entry.split()[1])

    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

    # Ensure all arrays are the same length
    vehicles =[cars,giants,motors]
    return vehicles

def getDate():
    date = []
    traffic_folder = "traffic"  # Folder containing the traffic data files
    for root, dirs, files in os.walk(traffic_folder):
        for file in files:
            if file.startswith("vehicles_") and file.endswith(".txt"):
                date_part = file.split('_')[1].split('.')[0]
                date.append(date_part)
    return date

  
locationDict = {
  "Highway A1":"loc01",
  "Vo Van Kiet":"loc02",
  "Phu Mi Bridge ":"loc03",
  "Binh Trieu Intersection":"loc04",
  "Long Thanh - Dau Giay":"loc05",
  "Highway 22":"loc06",
  "Binh Phuoc Intersection":"loc07",
  "Linh Xuan Intersection":"loc08",
  "Hang Xanh":"loc09",
  "Highway A1 - Kha Van Can":"loc10",
}