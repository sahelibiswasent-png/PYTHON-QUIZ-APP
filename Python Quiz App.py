"""PYTHON QUIZ APP
"""
QUESTIONS = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. list"],
        "answer": "C"
    },
    {
        "question": "Which symbol starts a comment in Python?",
        "options": ["A. //", "B. <!--", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "Which method adds an item to a list?",
        "options": ["A. add()", "B. append()", "C. insertEnd()", "D. push()"],
        "answer": "B"
    },
    {
        "question": "Which loop is commonly used to iterate over a sequence?",
        "options": ["A. for", "B. repeat", "C. each", "D. loop"],
        "answer": "A"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["A. ^", "B. **", "C. exp()", "D. pow()"],
        "answer": "B"
    },
    {
        "question": "Which function returns the length of a string?",
        "options": ["A. size()", "B. length()", "C. len()", "D. count()"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["A. try", "B. catch", "C. except", "D. error"],
        "answer": "C"
    },
    {
        "question": "Which method converts a string to lowercase?",
        "options": ["A. lower()", "B. toLower()", "C. downcase()", "D. lowercase()"],
        "answer": "A"
    },
    {
        "question": "Which data structure is ordered and mutable?",
        "options": ["A. tuple", "B. list", "C. set", "D. dictionary"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0
    print("-------------Python Basics Quiz-----------------")
    for number, q in enumerate(QUESTIONS, start=1):
        print(f"\\n{number}. {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {q['answer']}")
    print(f"\\nYour score: {score}/{len(QUESTIONS)}")
    percentage = (score / len(QUESTIONS)) * 100
    print(f"Percentage: {percentage:.0f}%")

if __name__ == "__main__":
    run_quiz()
