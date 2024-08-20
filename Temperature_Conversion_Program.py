import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    value = entry.get().upper()
    try:
        if "C" in value:
            C = float(value[:-1])
            K = C + 273.15
            F = (C * (9 / 5)) + 32
        elif "F" in value:
            F = float(value[:-1])
            C = (F - 32) * 5 / 9
            K = (F + 459.67) * 5 / 9
        elif "K" in value:
            K = float(value[:-1])
            C = K - 273.15
            F = (K * 9 / 5) - 459.67
        else:
            raise ValueError

        result_label.config(text=f"{C:.2f}°C, {F:.2f}°F, {K:.2f}K")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid temperature with a unit (e.g., 100C, 212F, 373K).")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x200")
root.configure(bg="lightblue")

# Create and place the input field and button
entry_label = tk.Label(root, text="Enter temperature value with unit (C, F, K):", bg="lightblue", font=("Arial", 12))
entry_label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_temperature, font=("Arial", 12), bg="blue", fg="white")
convert_button.pack(pady=10)

# Create and place the result label
result_label = tk.Label(root, text="", bg="lightblue", font=("Arial", 14))
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
