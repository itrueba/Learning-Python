from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def main():
    question_bank = []
    
    for question in question_data:
        text = question["text"]
        answer = question["answer"]
        question_bank.append(Question(text, answer))
    
    quiz = QuizBrain(question_bank)
    
    while quiz.still_has_question():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")

main()