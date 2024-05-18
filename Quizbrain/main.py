from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()

if not quiz_brain.still_has_question():
    print("You have completed the quiz")
    print(f"Your score was {quiz_brain.score}/{len(quiz_brain.q_list)}")