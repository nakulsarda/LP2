#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"hi|hello",
        ["Hello!", "Hi there!", "How can I assist you today?"]
    ],
    [
        r"book a bus|bus booking",
        ["Sure! To which destination would you like to book a bus?"]
    ],
    [
        r"(.) to (.)",
        ["I can help you find available buses from %1 to %2 . Please provide the date of travel."]
    ],
    [
        r"hi|hello|hey",
        ["Hello", "Hey there",]
    ],
    [
        r"book a bus ticket",
        ["Sure, I can assist you with that. Please provide the source and destination locations, as well as the travel date."]
    ],
    [
        r"I want to travel from (.) to (.) on (.*)",
        ["Great! Let me check the availability of buses from %1 to %2 on %3."]
    ],
    [
        r"available buses",
        ["Here are the available buses for your selected route: \n1. Bus 1 \n2. Bus 2 \n3. Bus 3"]
    ],
    [
        r"book bus (\d+)",
        ["Bus %1 has been booked successfully. Please provide your contact details for ticket confirmation."]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1. Can you please provide your phone number?"]
    ],
    [
        r"phone number is (\d+)",
        ["Thank you for providing your contact details. Your ticket will be sent to %1. Have a pleasant journey!"]
    ],
    [
        r"quit",
        ["Thank you for using our Redbus chatbot. Goodbye!"]
    ],
    [
        r"(.*) 2023",
        ["Ok , I'll see if any buses are available. Yes available ! Do you want to book a bus on %1"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand. Could you please rephrase your query?"]
    ]
]
chatbot = Chat(pairs, reflections)
def chat():
    print("Welcome to RedBus customer support. How can I assist you today?")
    while True:
        user_input = input("> > > ")
        print(" ")
        if user_input.lower() == "exit":
            break
        response = chatbot.respond(user_input)
        print(response)
        print(" ")
chat()


# In[ ]:




