# Chatbot

This is a simple chatbot implemented in Python using the Natural Language Toolkit (nltk) library. The chatbot is capable of responding to user inputs with predefined responses based on keyword matching and simple logic.

## Features

- Responds to user inputs with predefined responses.
- Uses nltk for text processing.
- Simple keyword-based response system.

## Requirements

- Python 3.x
- nltk

## Installation

1. Clone this repository:

```sh
git clone https://github.com/yourusername/chatbot.git
Navigate to the project directory:
sh
Copy code
cd chatbot
Install the required dependencies:
sh
Copy code
pip install nltk
Download the necessary nltk data:
python
Copy code
import nltk
nltk.download('punkt')
nltk.download('wordnet')
Usage
Run the chatbot.py script:

sh
Copy code
python chatbot.py
Example
python
Copy code
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['Hello %1, how are you today?']],
    ['(hi|hello|hey)', ['Hello!', 'Hey there!']],
    ['(.*) (location|city) ?', ['I am a chatbot, I live in the cloud.']],
    ['how is the weather in (.*)', ['I am not sure about the weather in %1, but I hope it is nice!']],
    ['quit', ['Bye! Take care.']]
]

def chatbot():
    print("Hi, I am the chatbot. Type 'quit' to exit.") 
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements.

License
This project is licensed under the MIT License.

Contact
For any questions or suggestions, please contact hariharanga1711@gmail.com
