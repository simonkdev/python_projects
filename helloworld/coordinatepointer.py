import pyautogui
import tkinter as tk

def update_coordinates():
    x, y = pyautogui.position()
    coord_label.config(text=f"X: {x}, Y: {y}")
    root.geometry(f"+{x+20}+{y+20}")
    root.after(100, update_coordinates)

def on_escape(event):
    root.destroy()

root = tk.Tk()
root.overrideredirect(True)  # Remove window decorations
root.attributes("-topmost", True)  # Keep the window on top

coord_label = tk.Label(root, font=("Helvetica", 12), bg="yellow")
coord_label.pack()

root.bind('<Escape>', on_escape)  # Bind the Escape key to the on_escape function

update_coordinates()
root.mainloop()
