THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class quizinterface:
    def __init__(self,quiz:QuizBrain):
        self.iquiz=quiz
        self.window=Tk()
        self.window.title("Quizzler")
        self.label=Label(text=f"Score:{self.iquiz.score}",fg="white",bg=THEME_COLOR,font=("Arial",12,"bold"))
        self.label.grid(row=0,column=1)
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canvas=Canvas(width=300,height=250)
        self.question_text=self.canvas.create_text(150,125,text="",fill=THEME_COLOR,font=("Arial",20,"normal"),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.right=PhotoImage(file="./images/true.png")
        self.button=Button(image=self.right,highlightthickness=0,command=self.true)
        self.button.grid(row=2,column=0)
        self.wrong=PhotoImage(file="./images/false.png")
        self.button1=Button(image=self.wrong,highlightthickness=0,command=self.false)
        self.button1.grid(row=2,column=1,padx=20,pady=20)
        self.get_new_question()
        self.window.mainloop()
    def get_new_question(self):
        self.canvas.config(bg="white")
        if self.iquiz.still_has_questions():
         q_text=self.iquiz.next_question()
         self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of quiz.")
            self.button.config(state="disabled")
            self.button1.config(state="disabled")
    def true(self):
        is_right=self.iquiz.check_answer("true")
        self.give_feedback(is_right)
    def false(self):
        self.give_feedback(self.iquiz.check_answer("false"))
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.label.config(text=f"Score:{self.iquiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_new_question)



