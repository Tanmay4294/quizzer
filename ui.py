from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=500, height=700)

        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 14, "bold")
        )
        self.score_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 20))

        self.canvas = Canvas(width=440, height=420, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            220,
            210,
            text="",
            width=360,
            fill="black",
            font=("Arial", 22, "italic"),
            justify="center"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0, pady=20)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"THE END\n\nFinal Score: {self.quiz.score}/{self.quiz.question_number}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback("True")

    def false_pressed(self):
        self.give_feedback("False")

    def give_feedback(self, answer):
        is_right = self.quiz.check_answer(answer)

        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(2000, self.get_next_question)
