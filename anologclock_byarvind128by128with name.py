# Import the modules
import tkinter as tk
import datetime
import math

# Create the main window
window = tk.Tk()
window.title("Analog Clock by arvind")

# Create a canvas to draw the clock
canvas = tk.Canvas(window, width=300, height=300, bg="black")
canvas.pack()

# Define the center and the radius of the clock
center_x = 150
center_y = 150
radius =   100
 # Create a text object on the canvas
canvas.create_text(center_x, center_y, text="by arvind", font=("Arial", 10), fill="black")

# Draw the clock face
canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill="lightblue", outline="black")

# Draw the hour marks
for i in range(12):
    # Calculate the angle and the position of each mark
    angle = math.radians(i * 30)
    x1 = center_x + radius * math.cos(angle)
    y1 = center_y + radius * math.sin(angle)
    x2 = center_x + (radius - 10) * math.cos(angle)
    y2 = center_y + (radius - 10) * math.sin(angle)
    # Draw a line from the edge to the center of the clock
    canvas.create_line(x1, y1, x2, y2, width=3)

# Define the length of the clock hands
hour_hand_length = 50
minute_hand_length = 70
second_hand_length = 80

# Define the tags for the clock hands
hour_hand_tag = "hour_hand"
minute_hand_tag = "minute_hand"
second_hand_tag = "second_hand"

# Define a function to update the clock
def update_clock():
    # Get the current time
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    # Calculate the angle of the hour hand
    hour_angle = math.radians(hour * 30 + minute * 0.5)

    # Calculate the position of the hour hand
    hour_x = center_x + hour_hand_length * math.cos(hour_angle)
    hour_y = center_y + hour_hand_length * math.sin(hour_angle)

    # Draw the hour hand
    canvas.delete(hour_hand_tag)
    canvas.create_line(center_x, center_y, hour_x, hour_y, width=3, fill="black", tag=hour_hand_tag)

    # Calculate the angle of the minute hand
    minute_angle = math.radians(minute * 6)

    # Calculate the position of the minute hand
    minute_x = center_x + minute_hand_length * math.cos(minute_angle)
    minute_y = center_y + minute_hand_length * math.sin(minute_angle)

    # Draw the minute hand
    canvas.delete(minute_hand_tag)
    canvas.create_line(center_x, center_y, minute_x, minute_y, width=3, fill="blue", tag=minute_hand_tag)

    # Calculate the angle of the second hand
    second_angle = math.radians(second * 6)

    # Calculate the position of the second hand
    second_x = center_x + second_hand_length * math.cos(second_angle)
    second_y = center_y + second_hand_length * math.sin(second_angle)

    # Draw the second hand
    canvas.delete(second_hand_tag)
    canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill="red", tag=second_hand_tag)

    # Schedule the function to run again after 100 milliseconds
    window.after(100, update_clock)
# Create a text object on the canvas
canvas.create_text(center_x, center_y, text="by arvind", font=("Arial", 16), fill="red")



# Call the function
update_clock()

# Start the main loop
window.mainloop()
