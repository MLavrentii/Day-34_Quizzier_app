from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class DataCollector:

    def __init__(self):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false)
        self.false_button.grid(row=2, column=0)
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def false(self):
        answer = "false"
        if self.quiz.still_has_questions():
            if self.quiz.check_answer(answer):
                self.update_score()
            self.get_next_question()
        else:
            q_text = f"Your final score was: {self.quiz.score}/{self.quiz.question_number}"

    def true(self):
        answer = "true"
        if self.quiz.still_has_questions():
            if self.quiz.check_answer(answer):
                self.update_score()
            self.get_next_question()
        else:
            q_text = f"Your final score was: {self.quiz.score}/{self.quiz.question_number}"