from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(width=300, height=500, padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=345, height=500)
        self.window.maxsize(width=345, height=500)
        
        self.score = Label(
            text=f'Score = 0', 
            fg='white', 
            bg=THEME_COLOR, 
            font=('Arial', '12', 'bold')
        )
        self.score.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
                150, 
                125, 
                text='Hi', 
                font=('Arial', '15', 'italic'),
                width=280
            )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        
        self.true_img = PhotoImage(file='images\\true.png')
        self.true_button = Button(image=self.true_img, width=100, height=97, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, pady=20)
        
        self.false_img = PhotoImage(file='images\\false.png')
        self.false_button = Button(image=self.false_img, width=100, height=97, command=self.false_pressed)
        self.false_button.grid(column=1, row=2, pady=20)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the game!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        
    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
        
    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)