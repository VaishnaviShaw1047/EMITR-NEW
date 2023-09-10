from flask import Flask, render_template, request, redirect, url_for,session
# from mongoutils import get_quiz_questions

app = Flask(__name__)

# A simple user database (replace with your actual user data)
users = {
    'username': 'password',
    'user2': 'password2'
}
marks_scored =0

@app.route('/')
def index():
    return render_template('instructions.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("enter login",request.method )
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
       
        if username in users and users[username] == password:
            return redirect(url_for('success',page=1))
        else:
            return redirect(url_for('failure'))

    return render_template('login.html')
@app.route('/failure')
def failure():
    return render_template('invalid_login.html')


quiz_data = [
    # Grammar Questions
    {
        "type": "Grammar",
        "question": "Which sentence is grammatically incorrect?",
        "options": [
            "She doesn't like neither pizza nor pasta.",
            "He is going to the store.",
            "They have been studying for hours.",
            "Neither John nor Mary have eaten dinner."
        ],
        "correct_Answer": "She doesn't like neither pizza nor pasta."
    },
    {
        "type": "Grammar",
        "question": "Choose the correct form of the verb to complete the sentence:\nShe _____ to the gym every day.",
        "options": [
            "go",
            "goes",
            "going",
            "went"
        ],
        "correct_Answer": "goes"
    },
    {
        "type": "Grammar",
        "question": "Identify the tense of the following sentence:\n\"I had visited the museum before it closed.\"",
        "options": [
            "Present",
            "Past",
            "Future",
            "Perfect"
        ],
        "correct_Answer": "Past"
    },
    {
        "type": "Grammar",
        "question": "Which of the following sentences is in the passive voice?",
        "options": [
            "She painted a beautiful picture.",
            "The book was read by him.",
            "They are playing soccer.",
            "He will bake a cake."
        ],
        "correct_Answer": "The book was read by him."
    },
    {
        "type": "Grammar",
        "question": "Choose the correct sentence:\nTheir car broke down, so they walked to the party.",
        "options": [
            "Their car broke down, so they walking to the party.",
            "Their car broken down, so they walked to the party.",
            "Their car broke down, so they walk to the party.",
            "Their car broke down, so they walks to the party."
        ],
        "correct_Answer": "Their car broke down, so they walked to the party."
    },
    
    # Comprehension Questions
    {
        "type": "Comprehension",
        "question": "What is the main idea of the passage?\n\"In recent years, climate change has become a pressing global issue. Rising temperatures, melting ice caps, and extreme weather events are all signs of this phenomenon.\"",
        "options": [
            "The causes of climate change",
            "The effects of climate change",
            "The urgency of addressing climate change",
            "The history of climate change"
        ],
        "correct_Answer": "The effects of climate change"
    },
    {
        "type": "Comprehension",
        "question": "Who is the author of the book mentioned in the passage?\n\"The book 'To Kill a Mockingbird' is a classic of American literature.\"",
        "options": [
            "The passage doesn't mention the author.",
            "Mark Twain",
            "Harper Lee",
            "J.K. Rowling"
        ],
        "correct_Answer": "Harper Lee"
    },
    {
        "type": "Comprehension",
        "question": "What is the central theme of the novel '1984' by George Orwell?",
        "options": [
            "Love and romance",
            "Totalitarianism and surveillance",
            "Adventure and exploration",
            "Family and relationships"
        ],
        "correct_Answer": "Totalitarianism and surveillance"
    },
    {
        "type": "Comprehension",
        "question": "What is the main conflict in Shakespeare's play 'Hamlet'?",
        "options": [
            "A family feud",
            "A love triangle",
            "Political power struggle",
            "Revenge and betrayal"
        ],
        "correct_Answer": "Revenge and betrayal"
    },
    {
        "type": "Comprehension",
        "question": "In the passage, what does the author suggest is the solution to the problem described?",
        "options": [
            "Increased government regulation",
            "Individual action and awareness",
            "Global economic reform",
            "Technological innovation"
        ],
        "correct_Answer": "Individual action and awareness"
    },
    
    # Nouns Questions
    {
        "type": "Nouns",
        "question": "Identify the plural form of 'child'.",
        "options": [
            "Childs",
            "Children",
            "Childes",
            "Child's"
        ],
        "correct_Answer": "Children"
    },
    {
        "type": "Nouns",
        "question": "Which of the following is a collective noun?",
        "options": [
            "Table",
            "Team",
            "Book",
            "Chair"
        ],
        "correct_Answer": "Team"
    },
    {
        "type": "Nouns",
        "question": "What is the plural form of 'deer'?",
        "options": [
            "Deers",
            "Deer",
            "Dears",
            "Deeres"
        ],
        "correct_Answer": "Deer"
    },
    {
        "type": "Nouns",
        "question": "Which word is a common noun?",
        "options": [
            "New York",
            "Eiffel Tower",
            "Dog",
            "Mars"
        ],
        "correct_Answer": "Dog"
    },
    {
        "type": "Nouns",
        "question": "Identify the possessive form of 'cat' in the sentence:\nThe cat's tail is fluffy.",
        "options": [
            "Cat's",
            "Cats'",
            "Cats",
            "Cats's"
        ],
        "correct_Answer": "Cat's"
    },
    
    # Vocabulary Questions
    {
        "type": "Vocabulary",
        "question": "Which word is the antonym of 'benevolent'?",
        "options": [
            "Malevolent",
            "Kind",
            "Generous",
            "Altruistic"
        ],
        "correct_Answer": "Malevolent"
    },
    {
        "type": "Vocabulary",
        "question": "Choose the synonym for 'ubiquitous':",
        "options": [
            "Rare",
            "Common",
            "Specific",
            "Widespread"
        ],
        "correct_Answer": "Common"
    },
    {
        "type": "Vocabulary",
        "question": "Which of the following words is a synonym for 'loquacious'?",
        "options": [
            "Quiet",
            "Talkative",
            "Shy",
            "Reserved"
        ],
        "correct_Answer": "Talkative"
    },
    {
        "type": "Vocabulary",
        "question": "What is the opposite of 'opaque'?",
        "options": [
            "Transparent",
            "Solid",
            "Hazy",
            "Dull"
        ],
        "correct_Answer": "Transparent"
    },
    {
        "type": "Vocabulary",
        "question": "Choose the correct definition of 'ephemeral':",
        "options": [
            "Lasting a long time",
            "Short-lived",
            "Everlasting",
            "Permanent"
        ],
        "correct_Answer": "Short-lived"
    },
    
    # Voice Questions
    {
        "type": "Voice",
        "question": "What is the passive voice of the sentence: 'The chef is preparing the meal.'?",
        "options": [
            "The chef prepared the meal.",
            "The meal has been prepared by the chef.",
            "The meal is being prepared by the chef.",
            "The chef will prepare the meal."
        ],
        "correct_Answer": "The meal is being prepared by the chef."
    },
    {
        "type": "Voice",
        "question": "Which of the following sentences is in the active voice?",
        "options": [
            "The letter was written by him.",
            "The cake was baked by her.",
            "The book was read by them.",
            "She sings beautifully."
        ],
        "correct_Answer": "She sings beautifully."
    },
    {
        "type": "Voice",
        "question": "Transform the following sentence into passive voice:\nThey built a new school in the town.",
        "options": [
            "A new school was built by them in the town.",
            "In the town, they built a new school.",
            "They were building a new school in the town.",
            "A new school has been built in the town."
        ],
        "correct_Answer": "A new school was built by them in the town."
    },
    {
        "type": "Voice",
        "question": "Change the following sentence to active voice:\nThe cake was eaten by the children.",
        "options": [
            "The children ate the cake.",
            "The cake has been eaten by the children.",
            "The children were eating the cake.",
            "The cake will be eaten by the children."
        ],
        "correct_Answer": "The children ate the cake."
    },
    {
        "type": "Voice",
        "question": "What is the active voice of the sentence: 'The movie was watched by the audience.'?",
        "options": [
            "The audience watched the movie.",
            "The movie is watched by the audience.",
            "The movie will be watched by the audience.",
            "The movie has been watched by the audience."
        ],
        "correct_Answer": "The audience watched the movie."
    },
]

page_mapping = {
    1: "Grammar",
    2: "Vocabulary",
    3: "Comprehension",
    4: "Nouns",
    5: "Voice"
    # Add more mappings as needed
}

def get_questions_by_type(questions, target_type):
    # Filter questions based on the target type
    filtered_questions = [q for q in questions if q['type'] == target_type]

    # Return the filtered questions
    return filtered_questions

@app.route('/success/<int:page>',methods=['GET', 'POST'])
def success(page):
    print("the page no we want",page)
    if page is None:
        page = 1
    if page>len(page_mapping):
        return redirect(url_for('quiz_completion'))

    # Calculate the type based on the page number
    type = page_mapping[page]
    print(page,type)

    # Get all questions of the specified type
    questions = get_questions_by_type(quiz_data, type)

    # Calculate the total number of questions
    total_questions = len(quiz_data)

    # Calculate the questions answered and marks scored up to the previous page
    questions_answered = 0
    global marks_scored # Initialize marks to 0
    print("method",request.method)
    if page > 1:
        for i in range(1, page):
            print("request form",request.form)
            values_list = [item[1] for item in request.form.items()]
            print("list",values_list)
            page_type = page_mapping[i]
            page_questions = get_questions_by_type(quiz_data, page_type)
            questions_answered += len(page_questions)
            for j in range(len(page_questions)):
                try:
                    user_answer = values_list[j]
                    print(user_answer,page_questions[j]['correct_Answer'])
                    if user_answer == page_questions[j]['correct_Answer']:
                        marks_scored += 5
                except:
                    marks_scored+=5

    # Calculate the percentage of questions remaining to attempt
    remaining_questions = total_questions - questions_answered - len(questions)
    percentage_remaining = (remaining_questions / total_questions) * 100

    # Get questions for the current page
    start_index = (page - 1) * len(questions)
    end_index = start_index + len(questions)
    page_quiz_data = questions
    print("records",marks_scored,percentage_remaining)
    
    return render_template('success.html', quiz_data=page_quiz_data, current_page=page, marks=marks_scored,next_page=page+1,
                           remaining=percentage_remaining,number_of_page=len(page_mapping))

@app.route('/quiz_completion')
def quiz_completion():
    # Check if the user is authenticated

    # Get marks and percentage completion from the session (modify this based on your session setup)
    marks_obtained = marks_scored
    total_marks = 100  # Replace 100 with the total marks available
    percentage_completion = (marks_obtained / total_marks) * 100

    # Define the congratulatory message or encouragement message based on the percentage obtained
    if percentage_completion >= 65:
        message = "Congratulations for clearing the exam!"
    else:
        message = "Better luck next time. Keep trying!"

    return render_template('quiz.html', marks_obtained=marks_obtained, 
                           total_marks=total_marks, percentage_completion=percentage_completion,
                           message=message)




if __name__ == '__main__':
    app.run(debug=True)