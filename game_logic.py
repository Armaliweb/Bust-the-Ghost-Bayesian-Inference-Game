import random
from config import GRID_COLS, GRID_ROWS, CONDITIONAL_TABLES, DIRECTION_TABLES

def place_ghost():
    # Randomly place the ghost on the grid
    xg = random.randint(0, GRID_ROWS - 1)
    yg = random.randint(0, GRID_COLS - 1)
    return xg, yg

def compute_initial_prior_probabilities():
    # Initialize the probability matrix with uniform probabilities
    total_cells = GRID_ROWS * GRID_COLS
    return [[1 / total_cells for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

def get_probabilities_for_distance(distance):
    # Sort distances in ascending order
    sorted_distances = sorted(CONDITIONAL_TABLES.keys())
    
    # Iterate in reverse order to find the largest key <= distance
    for d in reversed(sorted_distances):
        if distance >= d:
            return CONDITIONAL_TABLES[d]
    
    # If no key matches, return an empty dictionary (edge case)
    return {}

def distance_sense(x_click, y_click, ghost_x, ghost_y):
    """
    Calculate the Manhattan distance between the clicked cell and the ghost's position.
    Return a color based on the conditional probability table for the distance.
    """
    # Step 1: Calculate Manhattan distance
    distance = abs(x_click - ghost_x) + abs(y_click - ghost_y)
    
    # Step 2: Retrieve the probability dictionary for the calculated distance
    distance_probabilities = get_probabilities_for_distance(distance)

    # Step 3: Extract colors (keys) and probabilities (values) from the dictionary
    colors = list(distance_probabilities.keys())  # ["red", "orange", "yellow", "green"]
    probabilities = list(distance_probabilities.values())

    # Step 4: Use random.choices to select a color based on the probabilities
    selected_color = random.choices(colors, weights=probabilities)[0]
    return selected_color

def direction_sense(x_click, y_click, ghost_x, ghost_y):
    """
    Calculate the true direction of the ghost relative to the clicked cell
    and return a direction sampled based on the conditional probability table.
    """
    # Determine the true direction
    if x_click == ghost_x and y_click == ghost_y:
        true_direction = "Here"
    elif ghost_x > x_click:
        true_direction = "South"
    elif ghost_x < x_click:
        true_direction = "North"
    elif ghost_y > y_click:
        true_direction = "East"
    else:
        true_direction = "West"

    # Sample observed direction from the table
    direction_probabilities = DIRECTION_TABLES[true_direction]
    directions = list(direction_probabilities.keys())
    probabilities = list(direction_probabilities.values())
    observed_direction = random.choices(directions, weights=probabilities)[0]

    return observed_direction

def update_posterior_probabilities(color, x_click, y_click, probabilities):
    for row in range(len(probabilities)):
        for col in range(len(probabilities[row])):
            # Step 1: Calculate Manhattan distance
            distance = abs(x_click - row) + abs(y_click - col)

            # Step 2: Retrieve probabilities for the closest valid distance
            distance_probabilities = get_probabilities_for_distance(distance)

            # Step 3: Update the probability for the cell using the sensed color
            if color in distance_probabilities:
                probabilities[row][col] *= distance_probabilities[color]

    # Step 4: Normalize the probabilities
    total_prob = sum(sum(row) for row in probabilities)
    for row in range(len(probabilities)):
        for col in range(len(probabilities[row])):
            probabilities[row][col] /= total_prob
    return probabilities

def view(view_checked, probabilities, buttons):
    """Show or hide probabilities on the grid based on the view toggle."""
    for row in range(len(buttons)):
        for col in range(len(buttons[row])):
            if view_checked.get():
                prob = probabilities[row][col]
                # Use scientific notation if the number is very small
                if prob < 0.01:
                    buttons[row][col].config(text=f"{prob:.1e}")  # Scientific notation
                else:
                    buttons[row][col].config(text=f"{prob:.2f}")  # Decimal format
            else:
                buttons[row][col].config(text="")

def handle_bust(x_guess, y_guess, xg, yg, attempts):
    """Handle the bust logic."""
    if (x_guess, y_guess) == (xg, yg):
        return "win", attempts
    else:
        attempts -= 1
        return ("lose" if attempts == 0 else "continue"), attempts

def handle_cell_click(x_click, y_click, ghost_x, ghost_y, probabilities, score, direction_sensor_active):
    """
    Handle logic when a grid cell is clicked, considering both distance and direction sensors.
    """
    # Get distance and direction readings
    color = distance_sense(x_click, y_click, ghost_x, ghost_y)
    if direction_sensor_active:
        direction = direction_sense(x_click, y_click, ghost_x, ghost_y)
    else:
        direction = None

    # Update probabilities using the distance evidence
    probabilities = update_posterior_probabilities(color, x_click, y_click, probabilities)

    # If direction sensor is active, further refine the probabilities
    if direction_sensor_active:
        for row in range(len(probabilities)):
            for col in range(len(probabilities[row])):
                # Determine the true direction of this cell relative to the clicked cell
                if x_click == row and y_click == col:
                    true_direction = "Here"
                elif row > x_click:
                    true_direction = "South"
                elif row < x_click:
                    true_direction = "North"
                elif col > y_click:
                    true_direction = "East"
                else:
                    true_direction = "West"

                # Multiply by the likelihood of the observed direction
                probabilities[row][col] *= DIRECTION_TABLES[true_direction][direction]

        # Normalize probabilities again after direction evidence
        total_prob = sum(sum(row) for row in probabilities)
        for row in range(len(probabilities)):
            for col in range(len(probabilities[row])):
                probabilities[row][col] /= total_prob

    # Decrease the score
    score -= 1
    return color, direction, probabilities, score

def check_loss_condition(score, attempts):
    # Check if the game is lost based on score or attempts
    return score <= 0 or attempts <= 0