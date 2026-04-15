# from main import question_bank
# num= 0
# quiz_end = False
# for i in question_bank:
#     num += 1
#     Quiz =input(f"Q{num}:{i.text} (True/Flase):").lower()
#     if Quiz == i.answer.lower():
#         print("Correct")
#     else:
#         print("Incorrect")
#         break
#     if num == 12:
#         break



class Quiz_brain :

    def __init__(self,q_list ) :
        self.question_number = 0
        self.question_list = q_list
        self. score = 0

    def still_has_question(self):
        return  self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        question_number = self.question_number
        self.question_number += 1
        user_choice=input(f"Q{self.question_number}:{current_question .text} (True/Flase):")
        self.check_answer(user_choice, current_question.answer )


    def check_answer(self, user_choice, correct_answer ):
        if user_choice.lower() == correct_answer.lower():
            print(" You got it!")
            self.score +=1
        else :
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")





