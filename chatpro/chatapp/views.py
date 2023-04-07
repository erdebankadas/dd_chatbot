# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from .models import *

def chatbot(request):
    # Create object of ChatBot class with Logic Adapter
    bot = ChatBot(
        'Buddy',  
        logic_adapters=[
            'chatterbot.logic.BestMatch',
            'chatterbot.logic.TimeLogicAdapter'],
    )
    
    # Inport ListTrainer
    trainer = ListTrainer(bot)

    trainer.train([
    'Hi',
    'Hello',
    'I need your assistance regarding my order',
    'Please, Provide me with your order id',
    'I have a complaint.',
    'Please elaborate, your concern',
    'How long it will take to receive an order ?',
    'An order takes 3-5 Business days to get delivered.',
    'Okay Thanks',
    'No Problem! Have a Good Day!'
    ])
    
    if request.method == 'POST':
        message = request.POST['message']
        response = bot.get_response(message)
        return render(request, 'chatbot.html', {'message': message, 'response': response})
    else:
        return render(request, 'chatbot.html')




# from django.shortcuts import render
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from .models import *

# # Create a chatbot instance and train it on the corpus data
# bot = ChatBot('Buddy')
# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train('chatterbot.corpus.english')
# config = yaml.load(ymlfile, Loader=yaml.Loader)

# def chatbot(request):
#     if request.method == 'POST':
#         message = request.POST['message']
#         response = bot.get_response(message)
#         return render(request, 'chatbot.html', {'message': message, 'response': response})
#     else:
#         return render(request, 'chatbot.html')


