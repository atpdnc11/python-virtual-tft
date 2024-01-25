import tkinter as tk
from tkinter import Canvas
import math
import time

# TFT parameters
TFT_WIDTH = 320
TFT_HEIGHT = 240

# Define colors
ILI9341_BLACK = "black"
ILI9341_GREEN = "#00FF00"  # Green color code

class AnalogClock:
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(master, width=TFT_WIDTH, height=TFT_HEIGHT, bg=ILI9341_BLACK)
        self.canvas.pack()

        # Analog clock setup
        self.clock_center = (TFT_WIDTH // 2, TFT_HEIGHT // 2)
        self.clock_radius = min(TFT_WIDTH, TFT_HEIGHT) // 3
        self.hour_hand = None
        self.minute_hand = None

        # Main loop
        self.update_clock()

    def update_clock(self):
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min

        # Update hour hand
        hour_angle = math.radians((hours % 12) * 30 - 90)
        hour_x = self.clock_center[0] + int(self.clock_radius * 0.5 * math.cos(hour_angle))
        hour_y = self.clock_center[1] + int(self.clock_radius * 0.5 * math.sin(hour_angle))

        if self.hour_hand:
            self.canvas.delete(self.hour_hand)

        self.hour_hand = self.canvas.create_line(self.clock_center[0], self.clock_center[1], hour_x, hour_y, width=8, fill=ILI9341_GREEN)

        # Update minute hand
        minute_angle = math.radians(minutes * 6 - 90)
        minute_x = self.clock_center[0] + int(self.clock_radius * 0.8 * math.cos(minute_angle))
        minute_y = self.clock_center[1] + int(self.clock_radius * 0.8 * math.sin(minute_angle))

        if self.minute_hand:
            self.canvas.delete(self.minute_hand)

        self.minute_hand = self.canvas.create_line(self.clock_center[0], self.clock_center[1], minute_x, minute_y, width=4, fill=ILI9341_GREEN)

        # Set random background color
        random_color = "#{:02x}{:02x}{:02x}".format(
            int(127 + 128 * math.cos(time.time())),
            int(127 + 128 * math.sin(time.time())),
            int(127 + 128 * math.cos(time.time() * 0.5))
        )
        self.canvas.configure(bg=random_color)

        self.master.after(1000, self.update_clock)

root = tk.Tk()
root.title("Analog Clock with Random Background")
analog_clock = AnalogClock(root)
root.mainloop()
