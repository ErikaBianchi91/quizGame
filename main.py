from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#creo una lista dove inserire le domande
question_bank=[]
#ciclo sui dati nel file question_data

for question in question_data:
    question_t= question["text"]
    question_a= question["answer"]
    new_question= Question(question_t,question_a)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()
print("you've completed the quiz!")
print(f"your final score was {quiz.score}/{quiz.question_number}")