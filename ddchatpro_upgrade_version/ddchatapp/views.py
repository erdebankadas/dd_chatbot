from django.http import JsonResponse
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Load trained data from notepad
with open('ddchatapp/trained_data.txt', 'r') as file:
    trained_data = file.read().splitlines()

chatbot = ChatBot('MyBot')
trainer = ListTrainer(chatbot)
trainer.train(trained_data)


def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chatbot.get_response(message)
        return JsonResponse({'response': str(response)})
    return render(request, 'chat.html')
