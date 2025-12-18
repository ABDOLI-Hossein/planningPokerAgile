"""
@file main.py
@brief Point d'entrée de l'application Planning Poker.
"""
import tkinter as tk
from UI import PlanningPokerUI

def main():
    root = tk.Tk()
    app = PlanningPokerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()