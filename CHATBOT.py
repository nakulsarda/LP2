#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *

root = Tk()
root.title("Jio Mart Chatbot")

def send_message():
    user_input = entry.get().lower()
    message = "\nYou -> " + user_input
    chat_box.insert(END, message)

    if user_input == "hello":
        bot_response = "\nBot -> Hi! How can I assist you?"
    elif user_input == "browse products":
        bot_response = "\nBot -> Sure! Please select a category to browse products."
        # Implement logic for browsing products
    elif user_input == "add to cart":
        bot_response = "\nBot -> Okay! Please provide the details of the item you want to add to your cart."
        # Implement logic for adding items to cart
    elif user_input == "view cart":
        bot_response = "\nBot -> Sure! Here are the items in your cart."
        # Implement logic for viewing the cart
    elif user_input == "place order":
        bot_response = "\nBot -> Great! Please review your order and confirm to proceed."
        # Implement logic for placing an order
    elif user_input == "track order":
        bot_response = "\nBot -> Sure! Please provide your order ID to track your order."
        # Implement logic for tracking an order
    elif user_input == "cancel order":
        bot_response = "\nBot -> We're sorry to hear that you want to cancel your order."
        bot_response += "\nPlease provide your order ID to proceed with the cancellation."
        # Implement logic for canceling an order
    elif user_input == "talk to customer representative":
        bot_response = "\nBot -> You will now be connected to a customer representative."
        bot_response += "\nPlease wait while we connect you..."
        # Implement logic for connecting with a customer representative
    else:
        bot_response = "\nBot -> Sorry, I didn't understand. Can you please repeat?"

    chat_box.insert(END, bot_response)
    entry.delete(0, END)

# Create chat window
chat_box = Text(root)
chat_box.grid(row=0, column=0, columnspan=2)

# Create input field
entry = Entry(root, width=100)
entry.grid(row=1, column=0)

# Create send button
send_button = Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1)

root.mainloop()


# In[ ]:




