from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ai import ask_jarvis
from .models import ChatMemory


def home(request):
    return render(request, "index.html")


@csrf_exempt
def chat(request):

    if request.method == "POST":

        import json

        data = json.loads(request.body)

        user_message = data["message"]


        memory = ChatMemory.objects.all().order_by("-created_at")[:5]


        context = ""

        for chat in memory:

            context += f"""
            User: {chat.user_message}
            Jarvis: {chat.jarvis_reply}
            """


        reply = ask_jarvis(
            context + "\nUser: " + user_message
        )


        ChatMemory.objects.create(
            user_message=user_message,
            jarvis_reply=reply
        )


        return JsonResponse({
            "reply": reply
        })