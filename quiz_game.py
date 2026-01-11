# Basic Quiz Game
print("Welcome to the Quiz Game!\n")
    score = 0
questions =
[
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for AI and ML?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Personal Unit",
                    "C. Central Performance Unit", "D. Control Processing Unit"],
        "answer": "A"
    }
]
for q in questions:
    print(q["question"])
for option in q["options"]:
    print(option)
    
            user_answer = input("Your answer (A/B/C/D): ").upper()
    
if user_answer == q["answer"]:
   print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print(f"Quiz Over! Your final score is {score}/{len(questions)}")
