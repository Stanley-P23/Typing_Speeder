import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("600x400")  # You can adjust the window size as needed

# Configure columns to have equal weight so they expand equally
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

# Container frame for text_label
text_frame = tk.Frame(window, bg='pink', padx=30, pady=30)
text_frame.grid(column=1, columnspan=2, row=0, sticky='ew')  # Span columns 1 and 2, expand horizontally

# Entry
entry = tk.Entry(window, fg='white', bg="#FFD0D0", font=("Arial", 25, "normal"), borderwidth=0, width=44, justify='center')
entry.grid(column=1, columnspan=2, row=1, sticky='ew')  # Span columns 1 and 2, expand horizontally
entry.focus_set()

window.mainloop()