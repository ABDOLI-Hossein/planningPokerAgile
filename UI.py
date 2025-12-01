import tkinter as tk
from tkinter import simpledialog, messagebox

from session import Session
from story import Story


class PlanningPokerUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Planning Poker")
        self.root.geometry("600x500")

        # Default story + session
        self.story = Story("Default Story", "A simple default story")
        self.session = Session(self.story)

        # ------------------- STORY FRAME -------------------
        story_frame = tk.LabelFrame(root, text="Story", padx=10, pady=10)
        story_frame.pack(fill="x", padx=10, pady=5)

        self.story_label = tk.Label(story_frame, text=f"Current Story: {self.story.get_title()}")
        self.story_label.pack(side="left")

        tk.Button(story_frame, text="Change Story", command=self.change_story).pack(side="right")

        # ------------------- PLAYER FRAME -------------------
        player_frame = tk.LabelFrame(root, text="Players", padx=10, pady=10)
        player_frame.pack(fill="x", padx=10, pady=5)

        self.player_list = tk.Listbox(player_frame, height=4)
        self.player_list.pack(side="left", fill="both", expand=True)

        tk.Button(player_frame, text="Add Player", command=self.add_player).pack(side="right")

        # ------------------- CARD FRAME -------------------
        card_frame = tk.LabelFrame(root, text="Cards", padx=10, pady=10)
        card_frame.pack(fill="x", padx=10, pady=5)

        cards = ["1", "2", "3", "5", "8", "13", "21", "?"]
        for value in cards:
            btn = tk.Button(card_frame, text=value, width=5, command=lambda v=value: self.vote(v))
            btn.pack(side="left", padx=5)

        # ------------------- RESULTS FRAME -------------------
        results_frame = tk.Frame(root)
        results_frame.pack(pady=20)

        tk.Button(results_frame, text="Show Votes", command=self.show_results,
                  bg="lightblue", padx=20, pady=10).pack()

    # ----------- METHODS ---------------

    def change_story(self):
        title = simpledialog.askstring("Story Title", "Enter story title:")
        if title:
            description = simpledialog.askstring("Story Description", "Enter story description:")
            self.story = Story(title, description)
            self.session = Session(self.story)
            self.player_list.delete(0, tk.END)
            self.story_label.config(text=f"Current Story: {title}")

    def add_player(self):
        name = simpledialog.askstring("Add Player", "Enter player name:")
        if name:
            self.session.add_user(name)
            self.player_list.insert(tk.END, name)

    def vote(self, card_value):
        selected = self.player_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a player first!")
            return

        player_name = self.player_list.get(selected[0])
        self.session.add_vote(player_name, card_value)
        messagebox.showinfo("Vote Registered", f"{player_name} voted {card_value}")

    def show_results(self):
        results = "Votes:\n"
        for vote in self.session.get_votes():
            results += f"- {vote.get_user().get_name()} → {vote.get_card().get_value()}\n"

        messagebox.showinfo("Results", results)


# ---------- MAIN ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = PlanningPokerUI(root)
    root.mainloop()
