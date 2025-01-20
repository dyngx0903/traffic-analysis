import tkinter as tk
from tkinter import *
from ctypes import windll
from modules.dashboard import Dashboard
from PIL import Image, ImageTk

def init_window():
  windll.shcore.SetProcessDpiAwareness(1)

  #Start window (User Interface - UI)
  window = tk.Tk()

  window.title("Traffic App")
  window.geometry("1920x1080")
  window.configure(bg='#f5f5f5')
  p1 = PhotoImage(file = 'traffic/traffic-app-icon.png')
  window.iconphoto(False, p1)
  
  # Set the window to full-screen
  window.state('zoomed') # Maximize window
  
  # Add background image
  canvas = Canvas(window)
  canvas.pack(fill="both", expand=True)
  
  # Load the background image
  bg_image = Image.open("traffic/background.PNG")  # Image path
    
  # Position of the background image
  x_background = 300  
  y_background = 120  
  remaining_width = 1920 - x_background
  remaining_height = 1020 - y_background

  # Resize the image to fill the remaining space
  bg_image_resized = bg_image.resize((remaining_width, remaining_height), Image.Resampling.LANCZOS)
  bg_image_tk = ImageTk.PhotoImage(bg_image_resized)
  
   # Add the image to the canvas
  canvas.create_image(x_background, y_background, anchor="nw", image=bg_image_tk)
    
  # Store canvas and image as attributes of the window
  window.bg_canvas = canvas
  window.bg_image = bg_image_tk
  
  return window

if __name__ == "__main__":
    window = init_window()
    dashboard = Dashboard(window)
    window.mainloop()