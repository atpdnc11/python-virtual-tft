import tkinter as tk
import random

def rainbow_colors():
    return ["#FF0000", "#FFA500", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"]

class ScrollingText:
    def __init__(self, canvas, text, y, size):
        self.canvas = canvas
        self.text = text
        self.y = y
        self.size = size
        self.colors = rainbow_colors()
        self.label_ids = []

        for i, letter in enumerate(text):
            color = self.colors[i % len(self.colors)]
            label_id = canvas.create_text(i * size, y, text=letter, font=("Arial", size), fill=color, anchor=tk.W)
            self.label_ids.append(label_id)

        self.scroll_speed = 2
        self.canvas.after(30, self.scroll)

    def scroll(self):
        for label_id in self.label_ids:
            self.canvas.move(label_id, -self.scroll_speed, 0)
            coords = self.canvas.coords(label_id)
            if coords[0] + self.size < 0:
                self.canvas.coords(label_id, self.canvas.winfo_width(), coords[1])

        self.canvas.after(30, self.scroll)

class VirtualRGBMatrix:
    def __init__(self, master):
        self.master = master
        master.title("Combined App")

        # Set up canvas for scrolling text
        self.canvas_text = tk.Canvas(master, width=600, height=200, bg="black")
        self.canvas_text.pack()

        # Set up canvas for virtual RGB matrix
        self.canvas_matrix = tk.Canvas(master, width=32 * 20, height=8 * 20, bg="black")
        self.canvas_matrix.pack()

        # Create scrolling text
        scrolling_text_1 = ScrollingText(self.canvas_text, "ARVIND PATIL", 50, 20)
        scrolling_text_2 = ScrollingText(self.canvas_text, " LEARN BY SIMULATION", 100, 20)
        scrolling_text_3 = ScrollingText(self.canvas_text, " CALL 700336035 ", 150, 20)

        # Create virtual RGB matrix
        self.rgb_matrix = [[self.random_color() for _ in range(32)] for _ in range(8)]

        # Display the virtual RGB matrix
        self.display_matrix()

    def random_color(self):
        return "#{:02X}{:02X}{:02X}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def display_matrix(self):
        for row in range(8):
            for col in range(32):
                x1, y1 = col * 20, row * 20
                x2, y2 = x1 + 20, y1 + 20
                color = self.rgb_matrix[row][col]
                self.canvas_matrix.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def update_matrix(self):
        # Update virtual RGB matrix with new random colors
        self.rgb_matrix = [[self.random_color() for _ in range(32)] for _ in range(8)]

        # Redraw the matrix
        self.display_matrix()

        # Schedule the update for the next iteration
        self.master.after(1000, self.update_matrix)

root = tk.Tk()
app = VirtualRGBMatrix(root)
app.update_matrix()  # Start the matrix update loop
root.mainloop()
