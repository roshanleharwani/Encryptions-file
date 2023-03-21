import openai
import sys
from time import sleep

openai.api_key = open(r'C:\Users\rosha\Downloads\api.txt','r').read()
while 1:
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages = [{
            'role':'user',
            'content':str(input('>> '))
        }]

    )
    reply = str((dict(((response['choices'])[0])['message']))['content'])
    #print(reply)
    for char in reply:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    print( )
