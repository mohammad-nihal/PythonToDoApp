import json


with open("../Files/questions.json", 'r') as file:
    content = file.read()

print(content)
print(type(content))

data = json.loads(content)

print(data)
print(type(data))

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+ 1, "-" , alternative)
    user_choice=int(input("Enter answer: "))
    question["user_choice"] = user_choice  # Inject users choice into dictionary


score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    print(f"{result} {index+1} - Your answer: {question['user_choice']}, "
          f"Correct answer - {question['correct_answer']}")

print(score, '/' , len(data))