print("Welcome to computer science quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("\nOkay! Let's play :)")
score = 0

questions = {
    'What does CPU stand for? ': 'central processing unit',
    'What does GPU stand for? ': 'graphics processing unit',
    'What does RAM stand for? ': 'random access memory',
    'What does PSU stand for? ': 'power supply'
}

for question, correct_answer in questions.items():
    answer = input(question).lower()
    if answer == correct_answer:
        print('\nCorrect!')
        score += 1
    else:
        print("\nIncorrect!")

print("\nYou got " + str(score) + " questions correct!")
print("Your score is " + str((score / len(questions)) * 100) + "%.")
