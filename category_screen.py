####
# Group Number: HIT137_2023_S2_Group 8

# Group Members

# Shiraz Shrestha - S370167
# Maged Mohamed Esmat Mohamed - S367007
# Jemima Sodemba - S369931
# Sagar Khanal - S370166
####

import tkinter as tk
from quiz_screen import QuizScreen

# Create a CategoryScreen class that inherits from tk.Tk
class CategoryScreen(tk.Toplevel):
    def __init__(self, master, user_name):
        super().__init__(master)
        self.title('Select Category')   # Set the title of the window
        self.geometry('510x600')    # Set the initial window size
        
        self.setup_ui(user_name)
        
    def setup_ui(self, user_name):
        self.selected_category = None  
        self.user_name = user_name  
        
        # Label to display a welcome message with the user's name
        tk.Label(self, text=f'Welcome, {user_name}!', font=('Arial', 20)).pack(pady=30)
        
        # Label instructing the user to select a category
        tk.Label(self, text='Please select a category and click on START QUIZ', font=('Arial', 18, 'bold', 'italic'), background='red').pack(pady=15)
        
        # Label to display the selected category
        self.selected_label = tk.Label(self, text='Selected Category: None', font=('Arial', 15), foreground='yellow', bg='black')
        self.selected_label.pack(pady=20)
        
        # Create dictionary to map frame to its corresponding buttons
        frames_buttons = {
            "top_frame": ['Charles Darwin University', 'Northern Territory'],
            "bottom_frame": ['Australia', 'World']
        }
        
        for frame, buttons in frames_buttons.items():
            frm = tk.Frame(self)
            frm.pack(pady=10)
            for btn_text in buttons:
                # Create category selection buttons
                tk.Button(frm, text=btn_text, command=lambda b=btn_text: self.select_category(b), height=2, width=20, font=('Arial', 15)).pack(side='left', padx=10, pady=5)

        # Button to start the quiz        
        tk.Button(self, text='START QUIZ', command=self.start_quiz, height=2, width=20, font=('Arial', 18, 'bold')).pack(pady=20)
                
    def select_category(self, category):
        self.selected_category = category
        self.selected_label.config(text=f'Selected Category: {self.selected_category}')
    
    def start_quiz(self):
        if self.selected_category:
            # Start the quiz with the selected category
            QuizScreen(self.master, self.selected_category, self.user_name)
            self.destroy()  # Close the category selection window
        else:
            tk.messagebox.showinfo('Select a Category', 'Please select a category before starting the quiz')

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = CategoryScreen(root, 'Player')
    app.mainloop()
