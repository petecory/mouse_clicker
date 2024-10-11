import tkinter as tk
import pyautogui
import threading
import time
from pynput import keyboard

class MouseClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Clicker")
        self.root.geometry("300x200")  # Adjusted height to accommodate countdown label

        # Variable to control the click delay
        self.delay = tk.DoubleVar(value=1.0)  # Default is 1 second
        self.running = False

        # Create GUI elements
        self.create_widgets()

        # Set up the hotkey listener
        self.listener = keyboard.GlobalHotKeys({
            '<ctrl>+\'': self.stop_clicking
        })
        self.listener.start()

    def create_widgets(self):
        # Delay label and input
        label = tk.Label(self.root, text="Delay between clicks (seconds):")
        label.pack(pady=10)

        self.delay_entry = tk.Entry(self.root, textvariable=self.delay)
        self.delay_entry.pack(pady=5)

        # Start and Stop buttons
        start_button = tk.Button(self.root, text="Start Clicking", command=self.start_clicking)
        start_button.pack(pady=5)

        stop_button = tk.Button(self.root, text="Stop Clicking", command=self.stop_clicking)
        stop_button.pack(pady=5)

        # Countdown label
        self.countdown_label = tk.Label(self.root, text="")
        self.countdown_label.pack(pady=5)

    def start_clicking(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.start_countdown).start()

    def start_countdown(self):
        # 5-second countdown before clicking starts
        for i in range(5, 0, -1):
            self.update_countdown(f"Starting in {i} seconds...")
            time.sleep(1)
        self.update_countdown("")  # Clear the countdown label after countdown

        # Start clicking after the countdown
        self.click_mouse()

    def update_countdown(self, message):
        # Update the countdown label in the GUI
        self.countdown_label.config(text=message)

    def stop_clicking(self):
        self.running = False

    def click_mouse(self):
        # Get the delay from the input field
        try:
            delay = float(self.delay.get())
        except ValueError:
            delay = 1.0  # Default to 1 second if invalid input

        # Perform the clicking while `self.running` is True
        while self.running:
            pyautogui.click()
            time.sleep(delay)

def main():
    # Create the main window
    root = tk.Tk()
    app = MouseClickerApp(root)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
