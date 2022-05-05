from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
nlp=spacy.load('en')
chatbot= ChatBot('My bot')
conversation= [
    "hi",
    "hello",
    "want to buy electronic product",
    "which electronic poduct u want to buy?",
    "digital cameras",
    "which brand--sony , samsung or canon?",
    "canon",
    "any specifications?",
    "price range 10000 to 20000",
    "ok..wait"
    ]
trainer=ListTrainer(chatbot)
trainer.train(conversation)
print("chat with bot")
while True :
    query = input()
    if query!='bye':
        answer=chatbot.get_response(query)
        print(answer)
    if query=='bye':
        print('bye')
        break
