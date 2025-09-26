import tkinter as tk
from gui import create_gui, display_message
from game_logic import *
from config import INITIAL_SCORE, INITIAL_ATTEMPTS

def main():
    ghost_x, ghost_y = place_ghost()
    probabilities = compute_initial_prior_probabilities()
    score = INITIAL_SCORE
    attempts = INITIAL_ATTEMPTS
    last_clicked = None  # To store the coordinates of the last clicked cell

    def cell_click_handler(row, col):
        nonlocal score, probabilities, last_clicked, direction_checked

        last_clicked = (row, col)  # Update last clicked cell

        # Check if direction sensor is active
        direction_sensor_active = direction_checked.get()

        # Handle the cell click logic
        color, direction, probabilities, score = handle_cell_click(
            row, col, ghost_x, ghost_y, probabilities, score, direction_sensor_active
        )

        # Update the clicked button's border with the sensed color
        buttons[row][col].config(bg=color)

        # Optionally display direction information on the clicked button
        if direction_sensor_active:
            buttons[row][col].config(text=direction)

        # Update score label
        score_label.config(text=f"Score: {score}")

        # Refresh probabilities on the grid if "View" is active
        if view_checked.get():
            view(view_checked, probabilities, buttons)

        # Check for score-based loss
        if check_loss_condition(score, attempts):
            display_message(root, "You Lost!")


    def bust_handler():
        nonlocal attempts, last_clicked
        if last_clicked is None:
            display_message(root, "No cell clicked yet!")
            return

        x_guess, y_guess = last_clicked  # Use last clicked coordinates
        result, attempts = handle_bust(x_guess, y_guess, ghost_x, ghost_y, attempts)

        attempts_label.config(text=f"Attempts: {attempts}")
        if result == "win":
            display_message(root, "You Win!")
        elif result == "lose":
            display_message(root, "You Lose!")

    def view_handler():
        view(view_checked, probabilities, buttons)

    def toggle_sensor_handler():
        print("Direction Sensor toggled")

    root, score_label, attempts_label, view_checked, direction_checked, buttons = create_gui(
        bust_handler, cell_click_handler, view_handler, toggle_sensor_handler
    )

    root.mainloop()

if __name__ == "__main__":
    main()