
# 🖱️ Mouse Clicker with GUI

**Mouse Clicker** is a simple, user-friendly Python program designed to automate mouse clicks with customizable delay intervals. It features a GUI built using `tkinter`, allowing you to adjust the click delay, start and stop the clicker with ease, and includes a handy hotkey to stop the clicking (`Ctrl + '`).

## 🎉 Features

- **Adjustable Delay**: Customize the delay between each click in seconds.
- **Start/Stop Clicking**: Use GUI buttons to start or stop the clicking process.
- **Hotkey Support**: Stop the clicker using `Ctrl + '`.
- **5-Second Countdown**: After pressing the "Start Clicking" button, you get a 5-second countdown before the clicking begins—perfect for last-minute mouse positioning.
- **Cross-Platform**: Works on both Windows and Linux. (For Linux, it uses `pynput` to avoid requiring root access.)

## 📦 Requirements

This project requires Python 3.7+ and the following Python libraries:

- `tkinter`: For the graphical user interface.
- `pyautogui`: To control mouse clicks.
- `pynput`: For capturing the global hotkey.
  
You can install the required dependencies with:

```bash
pip install pyautogui pynput
```

## 🚀 Usage

1. **Clone the project**:
   ```bash
   git clone https://github.com/your-username/mouse_clicker.git
   cd mouse_clicker
   ```

2. **Install dependencies**:
   Make sure you have the required libraries installed by running:
   ```bash
   pip install pyautogui pynput
   ```

3. **Run the program**:
   Start the program by running:
   ```bash
   python mouse_clicker.py
   ```

4. **Adjust the settings**:
   - Set the delay between clicks in seconds in the GUI.
   - Press "Start Clicking" and you'll get a 5-second countdown before the clicks start.
   - Press "Stop Clicking" or use `Ctrl + '` to stop the automatic clicking at any time.

## 🛠️ Customization

Feel free to modify the program to fit your needs! Here are a few ideas:
- **Change the hotkey**: You can modify the `pynput` hotkey by adjusting the binding in the code.
- **Different click types**: Customize the `pyautogui.click()` function to include double-clicks, right-clicks, etc.
- **Extended countdown**: Change the countdown time to give yourself more (or less) time to prepare before the clicking starts.

## 🤔 How It Works

- **GUI**: The program's GUI is built with `tkinter`, giving you an interface to control the clicking process.
- **Mouse Automation**: The `pyautogui` library handles mouse automation, simulating clicks with the desired delay.
- **Hotkey**: The `pynput` library is used to listen for a global hotkey (`Ctrl + '`), allowing you to stop the clicker even if the GUI is out of focus.

## 🎮 Example Use Cases

- **Gaming**: Automate mouse clicks in idle games or during repetitive tasks.
- **Productivity**: Use it to perform repetitive mouse-clicking tasks like selecting multiple items, filling forms, etc.
- **Pranks**: Sneak it onto a friend's computer for some lighthearted mischief! 😜

## 📝 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Created by [Cory Peterson](https://github.com/petecory) – because sometimes, life just needs more clicking.
