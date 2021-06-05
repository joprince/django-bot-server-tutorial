import random

from django.shortcuts import render
from .models import Logs


def user(request):
    return render(request, 'chatbot_tutorial/user.html')


def chat(request):
    user_name = request.GET.get("user", "unknown")
    first = Logs.objects.get_or_create(user=user_name)
    context = {}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):
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
    data = Logs.objects.filter(user=message.get("user", "unknown")).first()
    if 'fat' in message['text']:
        data.fat_count += 1
        result_message['text'] = random.choice(jokes['fat'])

    elif 'stupid' in message['text']:
        data.stupid_count += 1
        result_message['text'] = random.choice(jokes['stupid'])

    elif 'dumb' in message['text']:
        data.dumb_count += 1
        result_message['text'] = random.choice(jokes['dumb'])

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message[
            'text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and " \
                      "i'll tell you an appropriate joke. "
    else:
        result_message[
            'text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, " \
                      "stupid or dumb. "
    data.save()
    return result_message


def logs(request):
    data = Logs.objects.all().values()
    context = {
        'data': data
    }
    return render(request, 'chatbot_tutorial/logs.html', context)
