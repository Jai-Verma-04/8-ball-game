from random import choice
from sys import exit

print('\n')

questions = ['What do you want to ask? ', 'What can i predict for you Today? ', 
'What can i help you with today? ', 'How can i help you today? ', 
'Hi, its good to hear from you..Ask your question. ','Hey there, how may I help you? ']

affirmative = ["Without a doubt!", "Most Likely", "my sources say YES!", "I'm Very sure its true", 
"YES", "Even God says Yes", "Of Course!"]

neutral = ['Maybe..', 'Who knows!', 'Follow your intuition', "Doubtful", "Perhaps", "Probably"]

negative = ['Try again some later time', "Hush! i'm a bit busy!", 
"Definitely not.", "Reply Hazy, Try again", "Don't count on it!", "My reply is No"]

lst = [affirmative, neutral, negative]

def prog():
    while True:
        answer = input(choice(questions))
        if len(answer)>0 and answer not in ('exit', 'quit'):
            print(">>",choice(choice(lst)))   
        elif len(answer)>0 and answer in ('exit', 'quit'):
            exit()
        else:
            print("Where was the Question? Concentrate and ask again")
            prog()
prog()