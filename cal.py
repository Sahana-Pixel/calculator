import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    
    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)
    
# Create the main window
root = tk.Tk()
root.title("Calculator")
calculator_bg_color = "#555555"  # Light gray
root.configure(bg=calculator_bg_color)

# Entry widget for display
entry = tk.Entry(root,bg="black",fg='white', width=20, font=("Arial", 25), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button color configuration
button_color = "#d9d9d9"  # Light gray
button_bg = "black"      # Off-white
button_active_bg = "gray"  # Light off-white
button_fg = "white"       # Dark gray
curve_radius = 5
# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+',
    
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, bg=button_bg, activebackground=button_active_bg,
              fg=button_fg,font=10, command=lambda btn=button: on_click(btn),borderwidth=20,
              border=curve_radius, highlightthickness=0).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter event loop
root.resizable(width=False, height=False)
root.mainloop()

