"""
MAGIC 8 BALL SIMULATOR for anybody to use.
"""

import random
import sys

#Dictionary of all the responses that the magic 8 ball may use
answer_dict={1:"It is certain.",
            2:"It is decidedly so.",
            3: "Without a doubt.",
            4:"Yes definitely.",
            5:"You may rely on it.",
            6:"As I see it, yes.",
            7:"Most likely.",
            8:"Outlook good.",
            9:"Yes.",
            10:"Signs point to yes.",
            11:"Reply hazy, try again.",
            12:"Ask again later.",
            13:"Better not tell you now.",
            14:"Cannot predict now.",
            15:"Concentrate and ask again.",
            16:"Don't count on it.",
            17:"My reply is no.",
            18:"My sources say no.",
            19:"Outlook not so good.",
            20:"Very doubtful."}
#Asking user to input name
name = input("Enter your name: ")
#If user doesn't capitalize first letter of name, program does it.
print(f"Welcome {name.capitalize()} to the Magic 8 Ball")

RUNNING = True

while RUNNING:
    #user inputs question
    question = input("Ask a question: ")
    answer = random.randint(1,20)
    #random library chooses a number 1-20 and gives out response
    answer_string = answer_dict[answer]
    print(answer_string)

    repeat = input("Ask another question? (y): ")
    #Loops to ask another question if user wants, else quit program
    if repeat == "y":
        RUNNING = True
    else:
        print("Thank you for playing the Magic 8 Ball! \nGoodbye!")
        sys.exit()
