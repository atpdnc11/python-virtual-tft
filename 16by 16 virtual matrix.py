import tkinter as tk
import time

class RGBMatrixSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("RGB Matrix Simulator")

        self.canvas = tk.Canvas(root, width=16 * 20, height=16 * 20, bg='black')
        self.canvas.pack()

        self.colors = ['red', 'green', 'blue']
        self.current_color_index = 0

        self.scroll_text(" virtual 16 x  16 matrix ", delay=0.4 )

    def scroll_text(self, text, delay):
        for i in range(16 * len(text)):
            self.canvas.delete("all")
            self.draw_matrix(i % 16, text)
            self.root.update()
            time.sleep(delay)

    def draw_matrix(self, offset, text):
        for i, char in enumerate(text):
            x = (i + offset) % 16
            y = 0
            color = self.colors[self.current_color_index]
            self.draw_pixel(x, y, color)
            self.canvas.create_text(x * 20 + 10, y * 20 + 10, text=char, fill='white', font=('Helvetica', 10, 'bold'))

    def draw_pixel(self, x, y, color):
        pixel_size = 20
        self.canvas.create_rectangle(x * pixel_size, y * pixel_size, (x + 1) * pixel_size, (y + 1) * pixel_size, fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    simulator = RGBMatrixSimulator(root)
    root.mainloop()
