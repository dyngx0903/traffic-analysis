from tkinter import *
import tkinter as tk
from datetime import *
from PIL import Image, ImageTk
import PIL
from tkinter import ttk, StringVar, OptionMenu, Text
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
from modules.trafficPrepare import getTraffic, locationDict, getDate
from modules.analyzer import data_analyzing

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.create_header()
        self.create_sidebar()
        self.create_controls()

    def create_header(self):
        header = tk.Frame(self.window, bg="#D2042D")
        header.place(x=300, y=0, width=1620, height=120)
        title = tk.Label(
            header, text="Traffic Capture in Ho Chi Minh City",
            font=("Roboto", 40, "bold"), fg='yellow', bg="#D2042D"
        )
        title.place(x=450, y=30)

    def create_sidebar(self):
        # Create the sidebar frame and store it as an instance attribute
        self.sidebar = tk.Frame(self.window, bg="#00539C")
        self.sidebar.place(x=0, y=0, width=300, height=1080)
        # Add an image to the sidebar
        image1 = Image.open("traffic/VGU.png")
        new_image1 = image1.resize((150, 150), PIL.Image.Resampling.LANCZOS)
        test = ImageTk.PhotoImage(new_image1)
        label1 = tk.Label(self.sidebar, image=test, borderwidth=0, relief="flat", background="#00539C")
        label1.image = test  # Keep a reference to avoid garbage collection
        label1.pack(side=tk.TOP, padx=20)

    def create_controls(self):
        self.clicked_date = StringVar()
        self.clicked_date.set('Select the date')
        dates = getDate()

        self.clicked_loc = StringVar()
        self.clicked_loc.set('Select the location')
        locations = list(locationDict.keys())
        
        tk.Label(text="Date:", bg="#00539C", fg="white", font=("Times New Roman", 18)).place(x=10, y=220)
        drop_date = OptionMenu(self.window, self.clicked_date, *dates)
        drop_date.place(x=70, y=220, width=200)

        tk.Label(text="Area:", bg="#00539C", fg="white", font=("Times New Roman", 18)).place(x=10, y=270)
        drop_loc = OptionMenu(self.window, self.clicked_loc, *locations)
        drop_loc.place(x=70, y=270, width=200)

        button = tk.Button(self.window, text="Graph", command=self.on_click)
        button.place(x=70, y=320, width=200, height=45)

    def on_click(self):
        date = self.clicked_date.get().strip('\t')
        loc = self.clicked_loc.get()
        destination = locationDict[loc]
        self.graph_traffic(date, destination)
    
    def graph_traffic(self, date, destination):
        # Hide background image when graph is displayed
        if hasattr(self.window, 'bg_canvas'):
            self.window.bg_canvas.pack_forget()

        # Initialize variables for tracking graphs
        if not hasattr(self, 'count'):
            self.count = 0

        # Clear previous graphs
        if self.count == 1:
            try:
                self.ax1.clear()
                self.graph_pointer.destroy()
                self.pie_pointer.destroy()
            except AttributeError as e:
                print(f"Error clearing previous graphs: {e}")

        # Create figures for bar and pie charts
        figure1 = plt.Figure(figsize=(10, 8), dpi=100, facecolor='#f5f5f5')
        figure2 = plt.Figure(figsize=(7, 7), dpi=100, facecolor='#f5f5f5')
        self.ax1 = figure1.add_subplot(111)
        ax2 = figure2.add_subplot(111)

        # Get traffic data
        traffic_data = getTraffic(date, destination)
        cars = traffic_data[0]
        giants = traffic_data[1]
        motors = traffic_data[2]
        
        time_labels = [
            '06:00\n-07:00', '07:00\n-08:00', '08:00\n-09:00', '09:00\n-10:00',
            '10:00\n-11:00', '11:00\n-12:00', '12:00\n-13:00', '13:00\n-14:00',
            '14:00\n-15:00', '15:00\n-16:00', '16:00\n-17:00', '17:00\n-18:00',
            '18:00\n-19:00', '19:00\n-20:00', '20:00\n-21:00'
        ]

        # Create DataFrame for bar chart
        df1 = pd.DataFrame({
            'Time': time_labels,
            'Motors': motors,
            'Cars': cars,
            'Giants': giants
        })
        
        # Set graph title
        for i in locationDict:
            if locationDict[i] == destination:
                locationTxt = i
        
        # Format date
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m-%Y")
        
        # Plot bar chart
        graph = FigureCanvasTkAgg(figure1, self.window)
        self.graph_pointer = graph.get_tk_widget()
        self.graph_pointer.place(x=310, y=150)
        df1.set_index('Time').plot(kind='bar', ax=self.ax1)
        self.ax1.set_xticklabels(time_labels, rotation=0)
        self.ax1.set_title(f"Traffic at {locationTxt} on {formatted_date}")
        self.ax1.set_ylim(0, max(max(motors), max(cars), max(giants)) * 1.1)

        # Prepare data for pie chart
        total_cars = sum(cars)
        total_giants = sum(giants)
        total_motors = sum(motors)
        vehicle_counts = [total_motors, total_cars, total_giants]
        vehicle_labels = ['Motors', 'Cars', 'Buses/Trucks']

        # Plot pie chart
        pie_chart = FigureCanvasTkAgg(figure2, self.window)
        self.pie_pointer = pie_chart.get_tk_widget()
        self.pie_pointer.place(x=1250, y=280)
        ax2.pie(vehicle_counts, labels=vehicle_labels, autopct='%1.1f%%', startangle=90)
        ax2.set_title("Vehicle Distribution")

        # Display analysis
        analysis_text = data_analyzing(traffic_data)
        text = Text(
            self.window, padx=25, pady=15, height=16, width=28,
            bg="#00539C", fg='yellow', font=("Times New Roman", 12, "bold")
        )
        text.insert('1.0', analysis_text)
        text.config(state='disabled')
        text.place(x=5, y=450)

        # Update count
        self.count = 1
