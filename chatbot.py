import nltk
from nltk.chat.util import Chat, reflections


# define pairs of patterbs and responses
pairs = [
    [
        r"my name is(.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"What's your name?",
        ["My name is Azula and i'm your chatbot.",]
    ],
    [
        r"How are you ?",
        ["I'm great \nHow about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","It's okay", "Never mind",]
    ],
    [
        r"i'm (.*) doing good|good|great|i'm fine",
        ["Nice to hear that","Good :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello","Hey there","Hi",]
    ],
    [
        r"(.*) age?|how old are you?",
        ["I'm a computer program, human hehehe"]
    ],
    [
        r"(.*) created you?",
        ["I was created by Habiba, using Pythin's NLTK library"]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is awesome like always","oh man, it's too hot here in %1"  ]
    ],
    [
        r"tell me a quote",
        ["The best way to predict the future is to create it. - Abraham Lincoln",
            "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
            "Life is what happens when you're busy making other plans. - John Lennon",
            "Be yourself; everyone else is already taken. - Oscar Wilde",
            "You only live once, but if you do it right, once is enough. - Mae West",
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "It does not matter how slowly you go as long as you do not stop. - Confucius",
            "Everything you can imagine is real. - Pablo Picasso",
            "In the midst of winter, I found there was, within me, an invincible summer. - Albert Camus"]
    ],
    [
        r"(quit|bye|goodbye|i've gotta go)",
        ["Bye take care. see you soon ;)","It was nice talking to you. see ya."]
    ]
]

# create chatbot
def chatbot():
    print("Hi, I'm Azula, a simple chatbot, How can i help you?",
        "if you wanna leave, just type quit.", sep="\n")
    
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__" :
    chatbot()