import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.chat.util import Chat, reflections

pairs = [
    ['hello|hey|hi', ['Hello!', 'Hi there!']],
    ['how are you', ['I am fine','I am doing well, thank you!', 'I am great, thanks for asking!']],
    ['bye|goodbye', ['Goodbye!', 'See you later!']]
]

chatbot = Chat(pairs, reflections)

chatbot.converse()