import requests
from click import progressbar
from gtts import gTTS
#from TTS.api import TTS
#from melo.api import TTS

parameters = {
    "amount": 10,
    "type": "boolean"
}
url = "https://opentdb.com/api.php"

class QuizData:
    def __init__ (self, parameters, url):
        self.parameters = parameters
        self.url = url

    def get_data(self):
        self.responses = requests.get(url=self.url, params=self.parameters)
        self.responses.raise_for_status()
        self.data = self.responses.json()
        self.question_data = self.data["results"]
        return self.question_data

responses = requests.get(url=url, params=parameters)
responses.raise_for_status()
data = responses.json()
question_data = data["results"]
print(data)
print(question_data)

# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The first computer bug was formed by faulty wires.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Linus Torvalds created Linux and Git.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "AMD created the first consumer 64-bit processor.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "'HTML' stands for Hypertext Markup Language.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]

tts_ = gTTS(text="I love you, baby!", lang="en")
tts_.save("output.mp3")


# model_path = ""
# tts = TTS(model_name=model_path, progressbar=False, gpu=False)
# tts.tts_to_file(text="Hello world", file_path="output.wav")

## # setup melo library:
## speed = 1.0
## device = "auto"
##
## text = "How are you doing?"
## model = TTS(language="EN_V2", device=device)
## speaker_ids = model.hps.data.spk2id
##
## # American accent
## output_path = "en-us.wav"
## model.tts_to_file(text, speaker_ids["EN-US"], output_path, speed=speed)
##
##
## # British accent
## output_path = 'en-br.wav'
## model.tts_to_file(text, speaker_ids['EN-BR'], output_path, speed=speed)