from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ai import ask_jarvis


def home(request):
    return render(request, "index.html")

@csrf_exempt
def chat(request):

        import json

        data = json.loads(request.body)

        user_message = data["message"]

        reply = ask_jarvis(user_message)

        return JsonResponse({
            "reply": reply
        })