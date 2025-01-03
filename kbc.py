import random
import emoji
from colorama import init,Fore,Style
init(autoreset=True)

def kbc():
    print(Style.BRIGHT + Fore.RED + "Welcome to the Kaun Bnega Crorepati!!")
    print(Fore.YELLOW + "The rules are as follows:")
    print(Style.BRIGHT + Fore.BLUE + "1. You will be asked a series of multiple-choice questions.")
    print(Style.BRIGHT + Fore.BLUE + "2. Each question has four options, only one of which is correct.")
    print(Style.BRIGHT + Fore.BLUE + "3. For each correct answer, you win a certain amount of money.")
    print(Style.BRIGHT + Fore.BLUE + "4. You can quit anytime and take the money you have won so far.")
    print(Style.BRIGHT + Fore.BLUE + "5. If you answer a question incorrectly, the game ends and you take home the money you have won up to the last correct answer.")
    print(Style.BRIGHT + Fore.YELLOW + "Good luck!")

    questions = [
        ["Which data structure is used to implement LIFO (Last In, First Out)?", "Queue", "Stack", "Array", "Linked List", "None", 2],
        ["Which keyword is used to define a function in Python?", "func", "function", "def", "lambda", "None", 3],
        ["What is the time complexity of searching in a balanced binary search tree (BST)?", "O(log n)", "O(n)", "O(1)", "O(n^2)", "None", 1],
        ["Which of these is a mutable data type in Python?", "String", "Tuple", "List", "Integer", "None", 3],
        ["What is the output of: print(2**3)?", "6", "8", "9", "16", "None", 2],
        ["Which sorting algorithm has the best average-case time complexity?", "Bubble Sort", "Selection Sort", "Quick Sort", "Merge Sort", "None", 4],
        ["In object-oriented programming, what does 'inheritance' mean?", "Using classes", "Defining objects", "Acquiring properties of another class", "Overriding methods", "None", 3],
        ["Which of the following languages is used for web development?", "HTML", "SQL", "C++", "Python", "None", 1],
        ["What is the output of: len({'a': 1, 'b': 2})?", "2", "1", "3", "4", "None", 1],
        ["Which of the following is a Python framework for web development?", "React", "Django", "Angular", "Flask", "None", 2]
    ]

    for question in questions:
        options = question[1:5]
        # print(options)
        correct_option = question[-1]
        # print(correct_option)
        correct_answer = options[correct_option - 1]
        # print(correct_answer)
        random.shuffle(options)
        question[1:5] = options
        # print(options)
        question[-1] = options.index(correct_answer) + 1
        # print(question[-1])

    levels = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 2560000, 512000]
    money = 0
    for i in range(0, len(questions)):
        question = questions[i]
        print(Fore.MAGENTA + f"\n\nQuestion for Rs. {levels[i]}")
        print(Fore.RED + f"{question[0]}")
        print(Fore.GREEN + f"a. {question[1]}          b. {question[2]} ")
        print(Fore.GREEN + f"c. {question[3]}          d. {question[4]} ")
        reply = int(input(Fore.YELLOW +"Enter your answer (1-4) or  0 to quit:\n"))
        if reply == 0:
            money = levels[i - 1]
            break
        if reply == question[-1]:
            print(emoji.emojize(f"Correct answer :check_mark_button:, you have won Rs. {levels[i]}"))
            money = levels[i]
        else:
            print(emoji.emojize(f"Wrong answer :cross_mark:, you have won Rs. {money} "))
            break

    print(Style.BRIGHT + Fore.RED + f"\nYou have won a total of Rs. {money}. Congratulations!")
kbc()