import requests
from click import progressbar
from gtts import gTTS
from data import QuizData

quiz_data = QuizData()
data = quiz_data.get_data()
print(data)

quiz_bank = {}

for question in data:
    q = question["question"]
    a = question["correct_answer"]
    quiz_bank[q] = a

print(quiz_bank)
#responses = requests.get(url=url, params=parameters)
#responses.raise_for_status()
#data = responses.json()
#question_data = data["results"]