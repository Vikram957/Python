import random
name = input("enter your name:")
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "How many states are there in India?",
        "options": ["A. 26", "B. 27", "C. 28", "D. 29"],
        "answer": "C"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What does len() do in Python?",
        "options": [
            "A. Adds numbers",
            "B. Finds the length",
            "C. Sorts a list",
            "D. Reverses a string"
        ],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "What is 10 % 3 in Python?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 0"],
        "answer": "A"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": [
            "A. Atlantic Ocean",
            "B. Indian Ocean",
            "C. Pacific Ocean",
            "D. Arctic Ocean"
        ],
        "answer": "C"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A. get()", "B. input()", "C. scan()", "D. read()"],
        "answer": "B"
    }
]
random.shuffle(questions)
score = 0
print("Welcome",name)
print("lets Start Quiz Game")
print("---------------")

for i in range(len(questions)):
    print("Question ",i+1)
    print(questions[i]["question"])

    for option in questions[i]["options"]:
        print(option)

    ans = input("enter your result in (A,B,C,D):").upper()

    if ans == questions[i]["answer"]:
        print("Correct")
        score+=1
    else:
        print("wrong!")
        print("right answer is:",questions[i]["answer"])

per = (score/len(questions))*100

print("======RESULT=====")
print("name:",name)
print("score:", score ,"/", len(questions))
print("percentage:",per)



if per >= 90:
    grade = "A+"
elif per >=75 and per < 90:
    grade = 'A'
elif per >= 60 and per <75:
    grade = 'B'
elif per >= 45 and per < 60:
    grade = 'C'
elif per >=33 and per <45:
    grade = 'D'
else:
    grade = "FAIL"

print("grade:",grade)


    
