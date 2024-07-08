
quiz_data = [

    {
        "genre": "Science",
        "question": "What is the chemical symbol for water?",
        "options": ["A. O2", "B. H2O", "C. CO2", "D. H2"],
        "correct_answer": "B"
    },
    {
        "genre": "Science",
        "question": "Who proposed the theory of relativity?",
        "options": ["A. Isaac Newton", "B. Galileo Galilei", "C. Albert Einstein", "D. Nikola Tesla"],
        "correct_answer": "C"
    },
    {
        "genre": "Science",
        "question": "What planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "correct_answer": "C"
    },
    

    {
        "genre": "Sports",
        "question": "Who has won the most Grand Slam titles in tennis?",
        "options": ["A. Roger Federer", "B. Rafael Nadal", "C. Novak Djokovic", "D. Pete Sampras"],
        "correct_answer": "B"
    },
    {
        "genre": "Sports",
        "question": "In which year did India win its first Cricket World Cup?",
        "options": ["A. 1975", "B. 1983", "C. 2007", "D. 2011"],
        "correct_answer": "B"
    },
    {
        "genre": "Sports",
        "question": "Who holds the record for the most goals in a single season of the English Premier League?",
        "options": ["A. Alan Shearer", "B. Thierry Henry", "C. Mohamed Salah", "D. Cristiano Ronaldo"],
        "correct_answer": "C"
    },


    {
        "genre": "Indian Current Affairs",
        "question": "Who is the current Prime Minister of India (as of 2024)?",
        "options": ["A. Narendra Modi", "B. Rahul Gandhi", "C. Amit Shah", "D. Arvind Kejriwal"],
        "correct_answer": "A"
    },
    {
        "genre": "Indian Current Affairs",
        "question": "Which Indian city is known as the Silicon Valley of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Bengaluru", "D. Hyderabad"],
        "correct_answer": "C"
    },
    {
        "genre": "Indian Current Affairs",
        "question": "In which year was the GST (Goods and Services Tax) implemented in India?",
        "options": ["A. 2014", "B. 2015", "C. 2016", "D. 2017"],
        "correct_answer": "D"
    },
    {
        "genre": "Indian Current Affairs",
        "question": "Who is the current President of India (as of 2024)?",
        "options": ["A. Ram Nath Kovind", "B. Pratibha Patil", "C. Droupadi Murmu", "D. Pranab Mukherjee"],
        "correct_answer": "C"
    }
]

def ask_question(question_data):
    """Asks a single question from the quiz and returns if the user's answer is correct."""
    print(f"Genre: {question_data['genre']}")
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    
    while True:
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")
    
    if user_answer == question_data["correct_answer"]:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong. The correct answer is {question_data['correct_answer']}.\n")
        return False

def run_quiz(quiz_data):
    """Runs the entire quiz, tracks the score, and gives feedback to the user."""
    score = 0
    total_questions = len(quiz_data)
    
    for question_data in quiz_data:
        if ask_question(question_data):
            score += 1
    
    print(f"Your final score is {score}/{total_questions}.")

def main():
    while True:
        run_quiz(quiz_data)
        try_again = input("Would you like to try again? (yes/no): ").strip().lower()
        if try_again != "yes":
            break

if __name__ == "__main__":
    main()
