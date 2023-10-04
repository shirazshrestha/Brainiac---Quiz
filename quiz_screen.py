####
# Group Number: HIT137_2023_S2_Group 8

# Group Members

# Shiraz Shrestha - S370167
# Maged Mohamed Esmat Mohamed - S367007
# Jemima Sodemba - S369931
# Sagar Khanal - S370166
####

import tkinter as tk
from tkinter import Label, Button, Frame, StringVar, messagebox
import csv
import os
from functools import partial

# Create a QuizScreen class that inherits from tk.Toplevel
class QuizScreen(tk.Toplevel):
    def __init__(self, master, category, user_name):
        super().__init__(master)
        self.title('Quiz Screen')
        self.geometry('510x600')
        
        self.category = category
        self.score = 0
        self.current_question_index = 0
        
        self.questions = self.load_questions(category)

        self.feedback_label = Label(self, text='', font=('Arial', 16), fg='red')  # New Label to show feedback
        self.feedback_label.pack(pady=10)

        self.user_name = user_name  # set user_name as an instance variable


        if not self.questions:
            messagebox.showerror('Error', f'No questions found for {category}!')
            self.destroy()
            return
        
        # Label to display the category
        Label(self, text=f'Category: {self.category}', font=('Arial', 18),fg='yellow',bg='black').pack(pady=10)
        
        # Label to display the score
        self.score_label = Label(self, text=f'Score: {self.score}', font=('Arial', 18), bg='green', bd=6, relief='ridge')
        self.score_label.pack(pady=10)
        
        # Label to display the question
        self.question_label = Label(self, text='', font=('Arial', 18, 'bold'), wraplength=500)
        self.question_label.pack(pady=10)
        
        self.selected_option = StringVar()
        
        self.options_frame = Frame(self)
        self.options_frame.pack(pady=20)
        
        self.display_question()
        
        # Button for moving to the next question
        self.next_button = Button(self, text='Next', state=tk.DISABLED, command=self.next_question, font=('Arial', 25))
        self.next_button.pack(pady=20)

    # Load questions from a CSV file based on the category
    def load_questions(self, category):
        questions = []
        script_dir = os.path.dirname(__file__)  # Get the directory of the current script
        file_path = os.path.join(script_dir, 'questions.csv')  # Construct the path to the CSV file

        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Category'] == category:
                        questions.append(row)
        except FileNotFoundError:
            messagebox.showerror('Error', 'Questions file not found!')
        return questions
    
    # Display the current question and options
    def display_question(self):
        self.feedback_label.config(text='')  # Clear feedback label when a new question is displayed
        question = self.questions[self.current_question_index]['Question']
        options = [self.questions[self.current_question_index][f'Option{i}'] for i in ['A', 'B', 'C', 'D']]
        
        self.question_label.config(text=question)
        
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        for option in options:
            btn = Button(self.options_frame, text=option, font=('Arial', 16), 
                         command=partial(self.check_answer, option), 
                         height=2, width=22, relief='solid')
            btn.pack(pady=5)
    
    # Check the selected answer and provide feedback
    def check_answer(self, chosen_option):
        self.next_button.config(state=tk.NORMAL)  # Enable the "Next" button once an option is selected.
        correct_answer = self.questions[self.current_question_index]['CorrectAnswer']
        if chosen_option == correct_answer:
            # Label to display feedback on the screen.
            self.feedback_label.config(text='Correct Answer!', fg='green', font=('Arial', 20))
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')
        else:
            # Label to display feedback on the screen.
            self.feedback_label.config(text=f'Incorrect Answer!\nThe correct answer was: {correct_answer}', fg='red', font=('Arial', 20))   

    # Move to the next question
    def next_question(self):
        self.next_button.config(state=tk.DISABLED)
        correct_answer = self.questions[self.current_question_index]['CorrectAnswer']
        selected_option = self.selected_option.get()  # Store the selected option before resetting
        
        # Compare the stored selected option with the correct answer
        if selected_option.strip().lower() == correct_answer.strip().lower():
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')
            self.feedback_label.config(text='Correct Answer!', fg='green', font=('Arial', 20))
        else:
            self.feedback_label.config(text=f'Incorrect! Correct Answer: {correct_answer}', fg='red', font=('Arial', 20))
        
        self.selected_option.set('')  # Reset the selected option for the next question
        
        self.current_question_index += 1  # Move to the next question
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.display_score_screen()

    # Method to display score screen    
    def display_score_screen(self):
        for widget in self.winfo_children():
            widget.destroy()  # remove all widgets from the current window
        
        greeting_text = f'Congratulations, {self.user_name}! 🎉'
        greeting_label = tk.Label(self, text=greeting_text, font=('Arial', 25))
        greeting_label.pack(pady=40)
        
        score_label = tk.Label(self, text=f'Your final score is {self.score}', font=('Arial', 25), bg='green')
        score_label.pack(pady=20)
        
        play_again_button = tk.Button(self, text='Play Again', font=('Arial', 20), height=2, width=22,command=self.play_again)
        play_again_button.pack(pady=15)
        
        exit_button = tk.Button(self, text='Exit Quiz', font=('Arial', 20), height=2, width=22,command=self.master.quit)
        exit_button.pack(pady=15)

    def play_again(self):
        from category_screen import CategoryScreen  # Import here to avoid circular imports
        self.destroy()  # Destroy the current window (Score Screen)
        category_screen = CategoryScreen(self.master, self.user_name)  # Create an instance of CategoryScreen, Pass user_name as an argument


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = QuizScreen(root, 'Charles Darwin University', 'Player') 
    app.mainloop()