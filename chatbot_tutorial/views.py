import random

from django.shortcuts import render
from .models import Logs


def user(request):
    """
    Function to handle user name on registration
    :param request: request from web page
    :return: webpage for user-name submission
    """
    context = {"user": "active",
               "logs": ""}
    return render(request, 'chatbot_tutorial/user.html', context)


def chat(request):
    """
    Function to handle request to chatbot
    :param request: request from webpage
    :return: webpage of the chatbot
    """
    user_name = request.GET.get("user", "None")
    first = Logs.objects.get_or_create(user=user_name)
    context = {}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):
    """
    Function to generate response for joke keywords
    :param message: message sent from user through bot
    :return: response containing the joke
    """
    jokes = {
        'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                   """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
        'fat': ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, 
                break it up!" """],
        'dumb': [
            """Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for 
            extra thick.""",
            """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""]
    }

    result_message = {
        'type': 'text'
    }
    message = message.content
    data = Logs.objects.filter(user=str(message.get("user"))).first()
    if 'fat' in message['text']:
        data.fat_count += 1
        result_message['text'] = random.choice(jokes['fat'])

    elif 'stupid' in message['text']:
        data.stupid_count += 1
        result_message['text'] = random.choice(jokes['stupid'])

    elif 'dumb' in message['text']:
        data.dumb_count += 1
        result_message['text'] = random.choice(jokes['dumb'])

    else:
        result_message[
            'text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, " \
                      "stupid or dumb. "
    data.save()
    return result_message


def logs(request):
    """
    Function to render the button logs
    :param request: request from webpage
    :return: rendered webpage of log table
    """
    data = Logs.objects.all().values()
    context = {
        'title': "Logs",
        'data': data,
        "user": "",
        "logs": "active"
    }
    return render(request, 'chatbot_tutorial/logs.html', context)
