questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Kathmandu", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "C"
    },
    {
        "prompt": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Hydrogen", "D. Helium"],
        "answer": "B"
    },
    {
        "prompt": "What is the powerhouse of the cell?",
        "options": ["A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Chloroplast"],
        "answer": "C"
    },
    {
        "prompt": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
        "answer": "C"
    },
    {
        "prompt": "Which country is known as the Land of the Rising Sun?",
        "options": ["A. Japan", "B. China", "C. Thailand", "D. India"],
        "answer": "A"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    }
]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)

        while True:
            answer = input("Enter your answer: A,B,C,D: ").upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input please enter A B C or D")

        if answer == question["answer"]:
            score += 1
            print("Your answer was correct!")

        else:
            print("Incorrect. The correct answer is:", question["answer"])

    print("Your final score is ", score, "out of ", len(questions))


run_quiz(questions)
