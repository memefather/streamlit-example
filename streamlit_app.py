from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openai

"""
# Welcome to SongQuiz! 🚀

What's the lyrics again? Let's test your musical knowledge!

"""
openai.api_key = os.getenv("OPENAI_API_KEY")
model_id = 'gpt-3.5-turbo'

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    # api_usage = response['usage']
    # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    # stop means complete
    # print(response['choices'][0].finish_reason)
    # print(response['choices'][0].index)
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

conversation = []
conversation.append({'role': 'system', 'content': 'You are playing a game with the user. The user will give you a line of lyric from a song. You will return the next line.'})
conversation = ChatGPT_conversation(conversation)
print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

def singnow():
    input = st.text_input('', 'Near, far, wheverever you are')

while input != '':
    prompt = input
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

if __name__ == '__main__':
    # call main function
    singnow()


    
