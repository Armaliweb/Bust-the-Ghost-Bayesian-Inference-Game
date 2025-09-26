# Bust the Ghost — Bayesian Inference Game

An AI-powered interactive game built in Python that demonstrates **Bayesian inference** for uncertainty reasoning.  
Developed as part of **CSC 4301: Introduction to Artificial Intelligence (Spring 2024)**.

---

##  Game Overview
- The game board is an **8×13 grid**.  
- A ghost hides randomly in one of the cells.  
- The player tries to find it by clicking cells and interpreting sensor clues.  
- The goal: **Bust the ghost before score or attempts run out!**

---

## Game Rules
- **Starting score**: 50 points.  
- **Bust attempts**: 2.  
- **Color hints (distance sensor)**:
  - 🔴 Red → Ghost is here  
  - 🟠 Orange → 1–2 cells away  
  - 🟡 Yellow → 3–4 cells away  
  - 🟢 Green → 5+ cells away  
- **Direction hints (direction sensor)**:
  - Provides noisy estimates of the ghost’s direction relative to the clicked cell.  

**Winning:** Bust the correct cell containing the ghost.  
**Losing:** Run out of score or bust attempts.  

---

## Implementation
The project is structured into 4 main Python files:

- `config.py` — game constants and conditional probability tables.  
- `gui.py` — Tkinter-based graphical interface.  
- `game_logic.py` — Bayesian inference, ghost placement, probability updates, and core rules.  
- `main.py` — main game loop, integrates GUI and logic.  

**Key Features**
- Bayesian inference updates ghost location probabilities after every sensor reading.  
- Probability view toggle — display posterior probabilities directly on the grid.  
- Direction sensor toggle — combine distance + direction evidence for refined inference.  

---

##  AI Concepts
- **Bayesian Inference** for updating beliefs about the ghost’s location.  
- **Conditional Probability Tables** for sensor reliability.  
- **Evidence Fusion** — combining distance and direction evidence.  

---

## How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/bust-the-ghost.git
   cd bust-the-ghost
