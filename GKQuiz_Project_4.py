def ask(question, answer):
    user = input(question + " ").strip().lower()
    return user == answer.lower()

def main():
    print("=== General Knowledge Quiz ===")
    score = 0
    questions = [
        ("What is the capital of France?", "paris"),
        ("Which planet is known as the Red Planet?", "mars"),
        ("Who developed Python programming language?", "guido van rossum")
    ]
    for q, a in questions:
        if ask(q, a):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {a.title()}\n")
    print(f"Final Score: {score}/{len(questions)}")
    if score == 3:
        print("Excellent!")
    elif score == 2:
        print("Good Job!")
    else:
        print("Keep Practicing!")

if __name__ == "__main__":
    main()
