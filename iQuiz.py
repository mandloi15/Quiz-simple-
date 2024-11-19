import random

questions = [
    {
        "question": "What is the output of print(2 + 2)?",
        "options": ["2", "4", "22", "Error"],
        "answer": "4"
    },
    {
        "question": "Which of the following is a valid Python variable name?",
        "options": ["1stVariable", "variable_1", "variable-1", "variable 1"],
        "answer": "variable_1"
    },
    {
        "question": "What keyword is used to create a function in Python?",
        "options": ["function", "def", "create", "func"],
        "answer": "def"
    },
    {
        "question": "In Java, what is the main method signature?",
        "options": ["public void main()", "public static void main(String[] args)", "void main()", "static void main()"],
        "answer": "public static void main(String[] args)"
    },
    {
        "question": "What does OOP stand for?",
        "options": ["Object-Oriented Programming", "Object-Oriented Process", "Object-Oriented Product", "Object-Oriented Protocol"],
        "answer": "Object-Oriented Programming"
    },
]

def user_authentication():
    print("Welcome to the Quiz!")
    action = input("Do you want to (L)ogin or (R)egister? ").strip().upper()
    
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    if action == 'R':
        print("Registration successful! You can now log in.")
    elif action == 'L':
        print("Login successful!")
    else:
        print("Invalid action. Exiting.")
        return None

    return email

def conduct_quiz(user_email):
    print(f"\nHello, {user_email}! Let's start the quiz.")
    score = 0
    selected_questions = random.sample(questions, 5)

    for question in selected_questions:
        print("\n" + question["question"])
        options = question["options"]
        random.shuffle(options)

        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        answer = input("Choose the correct answer (1-4): ")
        
        if options[int(answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question['answer']}")

    print(f"\nQuiz completed! Your score: {score} out of {len(selected_questions)}")

if __name__ == "__main__":
    user_email = user_authentication()
    if user_email:
        conduct_quiz(user_email)
