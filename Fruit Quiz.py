import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple', 'orange': 'orange', 'kiwi': 'brown', 'mango': 'yellow', 'blueberry': 'blue', 'strawberry': 'red', 'watermelon': 'green', 'peach': 'pink'}
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the colour of {} ?".format(fruit))
            user_answer = input()

            if (user_answer.lower() == color):
                print("Correct!")
            else:
                print("Wrong! The correct answer is {}".format(color))

            option = int(input("Enter 0 to continue or 1 to exit: "))
            if (option == 1):
                break
            else:
                continue    
print("Welcome to Fruit Quiz!")
fq = FruitQuiz()
fq.quiz()            