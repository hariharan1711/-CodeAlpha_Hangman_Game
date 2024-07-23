import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello, what can i do for you",]
    ],
    [
        r"what is your name?",
        ["I am a HEKAG chatbot.",]
    ],
    [
        r"how are you?",
        ["thank you for asking, i am fine",]
    ],
    [
        r"sorry (.*)",
        ["No problem!"]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear!", "Awesome, how can I assist you further?"]
    ],
    [
        r"(.*) age?",
        ["I am bot.",]
    ],
    [
        r"(.*) created you?",
        ["I was created by a developer using Python and NLTK.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm in the cloud, accessible from anywhere!",]
    ],
    [
        r"(.*) (sport|game) ?",
        ["I like to talk about different sports and games. What about you?",]
    ],
    [
        r"bye|quit|exit",
        ["Goodbye, have a great day!", "See you later!"]
    ],
]

def chatbot():
    print("Hi, I'm the  HEKAG chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
