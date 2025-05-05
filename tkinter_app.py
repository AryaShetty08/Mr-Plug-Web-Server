import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import matplotlib.pyplot as plt

class Leaderboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Mr. Plug - Energy Conservation Leaderboard")
        self.master.configure(bg="#bd9a7d")  # Brown background
        
        self.header_font = tkfont.Font(family="Helvetica", size=24, weight="bold")  # Larger header font with bold, using Helvetica font
        self.entry_font = tkfont.Font(family="Helvetica", size=12)  # Smaller entry font, using Helvetica font
        self.add_button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")  # Button font
        
        self.add_button = tk.Button(self.master, text="Add Player", command=self.add_player_name, font=self.add_button_font, bg="#6ea15f", fg="#000000", relief=tk.GROOVE, borderwidth=2, padx=10, pady=5, bd=0)  # Green button with black text, rounded corners
        self.add_button.pack(pady=10)
        
        self.personal_stats_button = tk.Button(self.master, text="Personal Stats", command=self.show_personal_stats, font=self.add_button_font, bg="#6ea15f", fg="#000000", relief=tk.GROOVE, borderwidth=2, padx=10, pady=5, bd=0)  # Green button with black text, rounded corners
        self.personal_stats_button.pack(pady=10)
        
        self.player_list = []
        self.scores = {}  # Dictionary to store player scores
        self.achievements = {}  # Dictionary to store earned achievements
        
        self.update_leaderboard()  # Display the leaderboard on initialization
        
    def add_player_name(self):
        add_player_window = tk.Toplevel(self.master)
        add_player_window.title("Add Player")
        add_player_window.configure(bg="#bd9a7d")  # Brown background
        
        player_name_label = tk.Label(add_player_window, text="Player Name:", font=self.entry_font, bg="#bd9a7d", fg="#000000")  # Brown background with black text
        player_name_label.grid(row=0, column=0, padx=10, pady=5)
        
        player_name_entry = tk.Entry(add_player_window, font=self.entry_font)
        player_name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        energy_score_label = tk.Label(add_player_window, text="Energy Conservation Score:", font=self.entry_font, bg="#bd9a7d", fg="#000000")  # Brown background with black text
        energy_score_label.grid(row=1, column=0, padx=10, pady=5)
        
        energy_score_entry = tk.Entry(add_player_window, font=self.entry_font)
        energy_score_entry.grid(row=1, column=1, padx=10, pady=5)
        
        submit_button = tk.Button(add_player_window, text="Submit", command=lambda: self.submit_score(add_player_window, player_name_entry.get(), energy_score_entry.get()), font=self.entry_font, bg="#8fbc8f", fg="#000000", relief=tk.GROOVE, borderwidth=2, padx=10, pady=5, bd=0)  # Green button with black text, rounded corners
        submit_button.grid(row=2, columnspan=2, pady=10)
        
    def submit_score(self, window, name, score):
        try:
            score = float(score)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the score.")
            return
        
        if name.strip() == "":
            messagebox.showerror("Error", "Please enter a valid name.")
            return
        
        self.scores[name] = score
        self.player_list.append((name, score))
        window.destroy()  # Close the add player window after submitting
        
        # Update leaderboard
        self.update_leaderboard()
        
    def update_leaderboard(self):
        # Sort player list by score in ascending order
        self.player_list.sort(key=lambda x: x[1])
        
        # Clear previous leaderboard display
        for widget in self.master.winfo_children():
            widget.destroy()
        
        # Display leaderboard
        header_label = tk.Label(self.master, text="Energy Conservation Leaderboard", font=self.header_font, bg="#bd9a7d", fg="#4b6e41")
        header_label.pack(pady=20)
        
        for idx, (name, score) in enumerate(self.player_list, start=1):
            player_label = tk.Label(self.master, text=f"{idx}. {name}: {score} kWh", font=self.entry_font, bg="#bd9a7d", fg="#000000")  # Brown background with black text
            player_label.pack()

        # Add Add Player button
        add_button = tk.Button(self.master, text="Add Player", command=self.add_player_name, font=self.add_button_font, bg="#8fbc8f", fg="#000000", relief=tk.GROOVE, borderwidth=2, padx=10, pady=5, bd=0)  # Green button with black text, rounded corners
        add_button.pack(pady=10)
        
        # Add Personal Stats button
        personal_stats_button = tk.Button(self.master, text="Personal Stats", command=self.show_personal_stats, font=self.add_button_font, bg="#8fbc8f", fg="#000000", relief=tk.GROOVE, borderwidth=2, padx=10, pady=5, bd=0)  # Green button with black text, rounded corners
        personal_stats_button.pack(pady=10)
        
        # Add Finish Adding button
        finish_button = tk.Button(self.master, text="Finish Adding", command=self.show_graph, font=self.add_button_font, bg="#8fbc8f", fg="#000000", relief=tk.GROOVE, borderwidth=2, padx=10, pady=5, bd=0)  # Green button with black text, rounded corners
        finish_button.pack(pady=10)
        
    def show_graph(self):
        if not self.player_list:
            messagebox.showerror("Error", "Please add at least one player.")
            return
        
        sorted_scores = sorted(self.player_list, key=lambda x: x[1], reverse=True)
        players = [name for name, _ in sorted_scores]
        scores = [score for _, score in sorted_scores]
        
        plt.figure(figsize=(8, 5))
        plt.plot(players, scores, marker='o', linestyle='', color='#7fad6e', label='Player Score')
        
        average_score = 203
        plt.axhline(y=average_score, color='r', linestyle='--', label='Average Score (203 kWh)')
        
        plt.title('Energy Conservation Leaderboard')
        plt.xlabel('Players')
        plt.ylabel('Energy Conservation Score (kWh)')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
    def show_personal_stats(self):
        personal_stats_window = tk.Toplevel(self.master)
        personal_stats_window.title("Personal Stats")
        personal_stats_window.configure(bg="#bd9a7d")  # Brown background
        
        player_name = "YourPlayerName"  # Placeholder for current user's name
        
        # Display past conservation efforts
        past_efforts_label = tk.Label(personal_stats_window, text=f"Past Conservation Efforts for {player_name}:", font=self.header_font, bg="#bd9a7d", fg="#000000")
        past_efforts_label.pack(pady=10)
        
        # Replace this section with actual data retrieval for the current user
        conservation_efforts = ["Effort 1", "Effort 2", "Effort 3"]
        for effort in conservation_efforts:
            effort_label = tk.Label(personal_stats_window, text=effort, font=self.entry_font, bg="#bd9a7d", fg="#000000")
            effort_label.pack()
        
        # Display earned badges
        badges_label = tk.Label(personal_stats_window, text="Earned Badges:", font=self.header_font, bg="#bd9a7d", fg="#000000")
        badges_label.pack(pady=10)
        
        # Replace this section with actual data retrieval for earned badges
        self.achievements = {"Badge 1": "Description 1", "Badge 2": "Description 2", "Badge 3": "Description 3"}
        for badge, description in self.achievements.items():
            badge_label = tk.Label(personal_stats_window, text=f"{badge}: {description}", font=self.entry_font, bg="#bd9a7d", fg="#000000")
            badge_label.pack()

def main():
    root = tk.Tk()
    leaderboard = Leaderboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()