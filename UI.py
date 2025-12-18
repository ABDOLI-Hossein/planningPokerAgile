"""
@file UI.py
@brief Interface Scrum Master avec gestion des rôles, Chronomètre de débat, Ajout Manuel et connexion Firebase.
"""
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from PIL import Image, ImageTk
import os
import time

# On importe la session qui contient la logique et la connexion Firebase
from session import Session

# --- CONFIGURATION GRAPHIQUE ---
COLORS = {
    "bg": "#2C3E50", "panel": "#34495E", "text": "#ECF0F1",
    "accent": "#E67E22", "success": "#27AE60", "danger": "#C0392B",
    "timer": "#F39C12"
}
FONTS = { "h1": ("Segoe UI", 16, "bold"), "h2": ("Segoe UI", 12, "bold"), "timer": ("Courier New", 40, "bold") }

class PlanningPokerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Planning Poker - Mode Manager")
        self.root.geometry("1000x850") 
        self.root.configure(bg=COLORS["bg"])
        
        self.session = Session()
        self.card_imgs = {}
        
        # Variables pour le chronomètre
        self.timer_running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.build_ui()

    def build_ui(self):
        # --- TOP BAR ---
        top_bar = tk.Frame(self.root, bg=COLORS["panel"], height=60)
        top_bar.pack(fill="x", side="top")
        
        self.create_btn(top_bar, "📂 Charger Backlog (JSON)", self.load_json, COLORS["accent"]).pack(side="left", padx=10, pady=10)
        
        # Indicateur de Mode
        self.lbl_mode = tk.Label(top_bar, text="Mode: Strict", bg=COLORS["panel"], fg=COLORS["text"], font=FONTS["h2"])
        self.lbl_mode.pack(side="right", padx=20)
        
        # --- MAIN AREA ---
        content = tk.Frame(self.root, bg=COLORS["bg"])
        content.pack(expand=True, fill="both", padx=20, pady=20)

        # GAUCHE : Ajout Manuel + Story + Liste Joueurs
        left_col = tk.Frame(content, bg=COLORS["bg"])
        left_col.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # 0. Zone d'Ajout Manuel
        manual_frame = tk.LabelFrame(left_col, text=" Ajout Rapide de Story ", font=FONTS["h2"], bg=COLORS["bg"], fg=COLORS["success"])
        manual_frame.pack(fill="x", pady=(0, 20))
        
        self.entry_manual_story = tk.Entry(manual_frame, font=("Segoe UI", 11))
        self.entry_manual_story.pack(side="left", fill="x", expand=True, padx=10, pady=10)
        
        self.create_btn(manual_frame, "Ajouter", self.add_manual_story, COLORS["success"]).pack(side="right", padx=10, pady=10)

        # 1. Story Panel
        self.story_frame = tk.LabelFrame(left_col, text=" Story en cours ", font=FONTS["h2"], bg=COLORS["bg"], fg=COLORS["accent"])
        self.story_frame.pack(fill="x", pady=(0, 20), ipady=10)
        
        self.lbl_title = tk.Label(self.story_frame, text="En attente...", font=FONTS["h1"], bg=COLORS["bg"], fg=COLORS["text"], wraplength=400, justify="left")
        self.lbl_title.pack(anchor="w", padx=10)
        self.lbl_desc = tk.Label(self.story_frame, text="...", font=("Segoe UI", 10), bg=COLORS["bg"], fg="#BDC3C7")
        self.lbl_desc.pack(anchor="w", padx=10)

        # 2. Players Panel (Avec Rôles)
        player_frame = tk.LabelFrame(left_col, text=" Participants ", font=FONTS["h2"], bg=COLORS["bg"], fg=COLORS["accent"])
        player_frame.pack(fill="both", expand=True)
        
        self.list_box = tk.Listbox(player_frame, bg=COLORS["panel"], fg=COLORS["text"], font=("Segoe UI", 11), selectbackground=COLORS["accent"])
        self.list_box.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.create_btn(player_frame, "👤 Ajouter Participant", self.add_player, COLORS["accent"]).pack(fill="x", padx=10, pady=10)

        # DROITE : Zone de Vote
        right_col = tk.LabelFrame(content, text=" Zone de Vote ", font=FONTS["h2"], bg=COLORS["panel"], fg=COLORS["text"])
        right_col.pack(side="right", fill="both", expand=True)

        self.cards_frame = tk.Frame(right_col, bg=COLORS["panel"])
        self.cards_frame.pack(expand=True)
        self.load_cards_grid()

        # --- BOTTOM ACTION ---
        self.btn_validate = tk.Button(self.root, text="🔒 RÉVÉLER LES VOTES (Manager)", font=FONTS["h1"], 
                                      bg=COLORS["danger"], fg="white", command=self.validate_turn, state="disabled")
        self.btn_validate.pack(side="bottom", fill="x", pady=0, ipady=10)


    # --- FONCTION : AJOUT MANUEL DE STORY ---
    def add_manual_story(self):
        text = self.entry_manual_story.get()
        if text:
            if hasattr(self.session, 'ajouter_story_manuelle'):
                self.session.ajouter_story_manuelle(text)
                self.entry_manual_story.delete(0, tk.END) 
                self.update_story() 
                
                # Feedback visuel
                self.lbl_title.config(fg=COLORS["success"])
                self.root.after(500, lambda: self.lbl_title.config(fg=COLORS["text"]))
            else:
                messagebox.showerror("Erreur Code", "La méthode 'ajouter_story_manuelle' n'existe pas dans session.py")
        else:
            messagebox.showwarning("Attention", "Veuillez écrire le sujet de la story.")

    # --- LOGIQUE DÉBAT / CHRONOMÈTRE ---
    
    def start_debate_mode(self, discord_msg):
        """Lance l'interface de débat qui cache le reste."""
        self.debate_win = tk.Toplevel(self.root)
        self.debate_win.title("🔴 Session de Débat")
        self.debate_win.geometry("800x600")
        self.debate_win.configure(bg="#2c3e50")
        self.debate_win.transient(self.root) 
        self.debate_win.grab_set() 

        # Titre
        tk.Label(self.debate_win, text="⚠️ DÉSACCORD DÉTECTÉ", font=("Arial", 20, "bold"), fg=COLORS["danger"], bg="#2c3e50").pack(pady=20)
        tk.Label(self.debate_win, text=discord_msg, font=("Arial", 12), fg="white", bg="#2c3e50").pack()

        # Chronomètre
        self.lbl_timer = tk.Label(self.debate_win, text="00:00", font=FONTS["timer"], fg=COLORS["timer"], bg="#2c3e50")
        self.lbl_timer.pack(pady=40)

        # Boutons
        btn_frame = tk.Frame(self.debate_win, bg="#2c3e50")
        btn_frame.pack(pady=20)

        self.create_btn(btn_frame, "Fin de réunion / Revoter", self.end_debate, COLORS["success"]).pack(side="left", padx=20)

        # Démarrer le timer
        self.start_time = time.time()
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        """Met à jour l'affichage du chrono."""
        if self.timer_running and hasattr(self, 'debate_win') and self.debate_win.winfo_exists():
            elapsed = int(time.time() - self.start_time)
            mins, secs = divmod(elapsed, 60)
            time_str = f"{mins:02}:{secs:02}"
            self.lbl_timer.config(text=time_str)
            self.root.after(1000, self.update_timer)

    def end_debate(self):
        """Arrête le débat et retourne au vote."""
        self.timer_running = False
        self.debate_win.destroy()
        
        self.session.reset_votes_for_retry()
        messagebox.showinfo("Nouveau Tour", "Les votes ont été remis à zéro. Veuillez revoter.")

    # --- LOGIQUE UI GÉNÉRALE ---

    def create_btn(self, parent, text, cmd, color):
        return tk.Button(parent, text=text, command=cmd, bg=color, fg="white", font=("Segoe UI", 10, "bold"), relief="flat", padx=10, pady=5)

    def load_cards_grid(self):
        vals = ["1", "2", "3", "5", "8", "13", "21", "?"]
        r, c = 0, 0
        for v in vals:
            path = f"assets/card_{'question' if v == '?' else v}.png"
            img = self.prepare_img(path)
            cmd = lambda val=v: self.vote(val)
            
            if img:
                b = tk.Button(self.cards_frame, image=img, bg=COLORS["panel"], command=cmd, bd=0)
                self.card_imgs[v] = img
            else:
                b = tk.Button(self.cards_frame, text=v, width=5, height=2, bg="white", command=cmd)
            b.grid(row=r, column=c, padx=10, pady=10)
            c += 1
            if c > 3: c=0; r+=1

    def prepare_img(self, path):
        if os.path.exists(path): return ImageTk.PhotoImage(Image.open(path).resize((80, 120)))
        return None

    def add_player(self):
        name = simpledialog.askstring("Nouveau", "Pseudo du participant :")
        if name:
            is_manager = messagebox.askyesno("Rôle", f"{name} est-il le MANAGER ?\n(Oui = Manager, Non = Voteur)")
            
            # --- MODIFICATION POUR FIREBASE ---
            # On crée un objet utilisateur simple
            user_obj = type('obj', (object,), {
                'name': name, 
                'is_manager': is_manager, 
                'get_name': lambda: name, 
                'get_role_name': lambda: "Manager" if is_manager else "Équipe"
            })
            
            # On utilise la nouvelle méthode 'register_user' qui gère Firebase
            self.session.register_user(user_obj)
            # ----------------------------------
            
            role_str = "[MANAGER] 👑" if is_manager else "[ÉQUIPE]"
            self.list_box.insert(tk.END, f"{role_str} {name}")
            
            if is_manager:
                self.btn_validate.config(state="normal", bg=COLORS["success"], text="🔒 RÉVÉLER LES VOTES")

    def vote(self, val):
        sel = self.list_box.curselection()
        if not sel:
            messagebox.showwarning("!", "Sélectionnez votre nom dans la liste !")
            return
            
        full_text = self.list_box.get(sel[0])
        name = " ".join(full_text.split(" ")[1:]) if "]" in full_text else full_text

        self.session.add_vote(name, val)
        messagebox.showinfo("Vote", f"{name} a voté (Vote caché).")

    def validate_turn(self):
        ok, msg = self.session.validate_round()
        
        if not ok and "Pause Café" not in msg and "Aucun vote" not in msg and "Aucune story" not in msg:
            self.start_debate_mode(msg)
        else:
            if not ok and "Aucune story" in msg:
                messagebox.showerror("Erreur", msg)
            else:
                messagebox.showinfo("Résultat", msg)
                if ok:
                    self.update_story()

    def update_story(self):
        s = self.session.current_story
        if s:
            titre = s.description if hasattr(s, 'description') else str(s)
            self.lbl_title.config(text=titre)
            self.lbl_desc.config(text="Story manuelle" if hasattr(s, 'estimation') else "")
        else:
            self.lbl_title.config(text="TERMINE / EN ATTENTE")
            self.lbl_desc.config(text="Ajoutez une story manuellement ou chargez un fichier.")

    def load_json(self):
        f = filedialog.askopenfilename()
        if f:
            self.session.load_data(f)
            self.update_story()

# --- BLOC DE LANCEMENT (Si vous lancez UI.py directement) ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PlanningPokerUI(root)
    root.mainloop()