from pymongo import MongoClient
from urllib.parse import quote_plus


def connect_to_mongodb():
    # Replace '<username>', '<password>', and '<dbname>' with your actual credentials
    username = "shawvaish"
    password = "vaishmongodb"
    dbname = "Languageproficencey"

    # URL-encode the username and password
    username = quote_plus(username)
    password = quote_plus(password)

    mongodb_uri = f"mongodb+srv://{username}:{password}@cluster.mongodb.net/{dbname}"

    client = MongoClient(mongodb_uri)
    return client

def get_quiz_questions():
    client = connect_to_mongodb()
    db = client.Languageproficency  # Use the correct database name
    collection = db.EnglishQuiz  # Use the correct collection name
    question_data = collection.find_one({"language": "english"})
    if question_data:
        return question_data.get("questions")
    else:
        return []

questions = get_quiz_questions()
for question in questions:
    print(question)