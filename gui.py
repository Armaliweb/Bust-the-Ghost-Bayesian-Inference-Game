import tkinter as tk
from tkinter import PhotoImage

def create_gui(bust_handler, cell_click_handler, view_handler, direction_sensor_handler):
    root = tk.Tk()
    root.title("Bust the Ghost")
    root.geometry("900x720")  # Initial window size

    # Load background image and keep a reference
    background_image = PhotoImage(file="./image.png")
    canvas = tk.Canvas(root, width=900, height=720)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")
    root.background_image = background_image  # Keep reference to avoid garbage collection

    # Button frame (top-left)
    button_frame = tk.Frame(root, bg="#2e2e2e")
    button_frame.place(relx=0.05, rely=0.05, anchor="nw")

    # Variables for the checkbuttons
    view_checked = tk.BooleanVar(value=False)
    direction_checked = tk.BooleanVar(value=False)

    # Checkbuttons for "View" and "Direction Sensor" with handlers
    view_checkbutton = tk.Checkbutton(
        button_frame,
        text="View",
        variable=view_checked,
        command=view_handler,
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#2e2e2e",
        activebackground="#2e2e2e",
        activeforeground="white",
        selectcolor="#2e2e2e",
        onvalue=True,
        offvalue=False,
    )
    view_checkbutton.pack(side="left", padx=10)

    direction_checkbutton = tk.Checkbutton(
        button_frame,
        text="Direction Sensor",
        variable=direction_checked,
        command=direction_sensor_handler,
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#2e2e2e",
        activebackground="#2e2e2e",
        activeforeground="white",
        selectcolor="#2e2e2e",
        onvalue=True,
        offvalue=False,
    )
    direction_checkbutton.pack(side="left", padx=10)

    # Bust button with handler
    bust_button = tk.Button(
        button_frame, text="Bust", font=("Arial", 12, "bold"), bg="DeepSkyBlue4", fg="white", width=11, command=bust_handler)
    bust_button.pack(side="left", padx=5)

    # Label frame (top-right)
    label_frame = tk.Frame(root, bg="#2e2e2e")
    label_frame.place(relx=0.95, rely=0.05, anchor="ne")

    score_label = tk.Label(label_frame, text="Score: 50", font=("Arial", 12, "bold"), fg="white", bg="#2e2e2e")
    score_label.pack(pady=5)

    attempts_label = tk.Label(label_frame, text="Attempts: 2", font=("Arial", 12, "bold"), fg="white", bg="#2e2e2e")
    attempts_label.pack(pady=5)

    # Grid (center)
    grid_frame = tk.Frame(root, bg="#2e2e2e")
    grid_frame.place(relx=0.5, rely=0.5, anchor="center")

    buttons = []
    for row in range(8):
        row_buttons = []
        for col in range(13):
            btn = tk.Button(
                grid_frame,
                text="",
                bg="lightgrey",
                width=7,
                height=3,   
                command=lambda r=row, c=col: cell_click_handler(r, c)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)
            row_buttons.append(btn)
        buttons.append(row_buttons)

    # Return the elements for further use in logic
    return root, score_label, attempts_label, view_checked, direction_checked, buttons

def display_message(root, message):
    message_window = tk.Toplevel(root)
    message_window.geometry("900x720")
    message_window.title("Game Over")

    message_label = tk.Label(
        message_window,
        text=message,
        font=("Arial", 20, "bold"),
        fg="red",
        bg="white",
        anchor="center"
    )
    message_label.pack(expand=True, fill="both")

    # Button to close the message and exit
    exit_button = tk.Button(
        message_window,
        text="Exit",
        command=root.destroy,
        font=("Arial", 14, "bold"),
        bg="red",
        fg="white"
    )
    exit_button.pack(pady=20)
