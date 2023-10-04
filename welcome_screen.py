####
# Group Number: HIT137_2023_S2_Group 8

# Group Members

# Shiraz Shrestha - S370167
# Maged Mohamed Esmat Mohamed - S367007
# Jemima Sodemba - S369931
# Sagar Khanal - S370166
####

import tkinter as tk
from category_screen import CategoryScreen
import os  # Import the os module for working with file paths

# Get the directory where the script is located
script_dir = os.path.dirname(__file__)

# Create a WelcomeScreen class that inherits from tk.Tk
class WelcomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Brainiac Quiz') # Set the title of the window
        self.geometry('510x600') # Set the initial window size
        
        # Load the quiz logo from an image file
        self.logo = tk.PhotoImage(file=os.path.join(script_dir, 'assets/logo.png')) 
        tk.Label(self, image=self.logo).pack(pady=20) # Display the logo in the window

        # Create a welcome label
        tk.Label(self, text='Welcome to Brainiac Quiz', font=('Arial', 22)).pack(pady=20)
        
        # Create a label to instruct the user to enter their name
        tk.Label(self, text='Enter your name', font=('Arial', 18), foreground='yellow', bg='black').pack(pady=10)
        
        # Create an entry field for the user's name
        self.name_entry = tk.Entry(self, width=20, font=('Arial', 25), bd=5, relief='ridge', justify='center')
        self.name_entry.pack(pady=5)
        
        # Create a frame for buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
         # Create a "Start" button that calls the start_quiz method
        tk.Button(button_frame, text='Start', command=self.start_quiz, font=('Arial', 20),height=2, width=14).pack(side='left', padx=10)

        # Create an "Exit" button that calls the exit_app method
        tk.Button(button_frame, text='Exit', command=self.exit_app, font=('Arial', 20),height=2, width=14).pack(side='left', padx=10)

    # Method to start the quiz    
    def start_quiz(self):
        user_name = self.name_entry.get().strip()  # Get the user's name and remove leading/trailing whitespace
        if user_name:
            self.withdraw() # Hide the current window
            CategoryScreen(self, user_name) # Create a CategoryScreen instance with the user's name
        else:
            tk.messagebox.showinfo('Error', 'Please enter your name before starting the quiz') # Show an error message if the name is empty

    # Method to exit the application
    def exit_app(self):
        self.destroy() # Destroy the main window
        
# Entry point of the application
if __name__ == "__main__":
    app = WelcomeScreen()   # Create an instance of the WelcomeScreen class
    app.mainloop()  # Start the tkinter main loop


         
