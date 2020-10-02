from quizc.console.quiz_ui_handler import *


class Menu(object):
    MENU_PROMPT = "> "

    def __init__(self):
        self.car = ""
        self.quiz = None
        self.quiz_answers = None

    def show_main_menu(self):
        print("""
Quizc - A command quiz utility
======================================
1. Create quiz
2. Fill quiz
3. Show quiz
4. Exit
======================================
        """)

#    def process(self):
#        self.show_main_menu()
#        option = input(self.MENU_PROMPT)
#        should_exit = False
#        if option == "1":
#            self.quiz = QuizUIHandler.create_quiz()
#        elif option == "2":
#            if self.quiz is None:
#                print("No quiz available, you must create first a quiz")
#            else:
#                self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)
#        elif option == "3":
#            if self.quiz_answers is None:
#                print("No filled quiz available, you must create first a quiz")
#            else:
#                QuizUIHandler.show_quiz(self.quiz_answers)
#        elif option == "4":
#            should_exit = True

#        return should_exit

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def option1(self, option):
        return option == "1"

    def option2(self, option):
        return option == "2"

    def option2_error(self, option):
        return option == "2" and self.quiz is None

    def option3(self, option):
        return

    def option3_error(self, option):
        return option == "3" and self.quiz_answers is None

    def option4(self, option):
        return option == "4"

    def options(self, option):
        should_exit = False

        if self.option1(option):
            self.quiz = QuizUIHandler.create_quiz()


        if self.option2_error(option):
            print("No quiz available, you must create first a quiz")

        # option=2
        if self.option2(option):
            self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)


        if self.option3_error:
            print("No filled quiz available, you must create first a quiz")

            # option =3
        if self.option3(option):
            QuizUIHandler.show_quiz(self.quiz_answers)

        if self.option4(option):
            should_exit = True

        return should_exit

    def process(self):
        self.show_main_menu()
        option = input(self.MENU_PROMPT)
        should_exit = self.options(option)

        return should_exit





