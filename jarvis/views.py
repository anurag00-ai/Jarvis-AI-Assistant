from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .ai import ask_jarvis, web_search
from .models import ChatMemory



def home(request):

    return render(request, "index.html")




@csrf_exempt
def chat(request):

    if request.method == "POST":


        import json


        data = json.loads(request.body)


        user_message = data["message"]



        # Internet search command

        if "search" in user_message.lower():


            query = user_message.lower().replace("search","").strip()


            results = web_search(query)


            reply = ask_jarvis(

                "Use this internet information to answer:\n\n"
                + results

            )



        else:


            reply = ask_jarvis(user_message)





        ChatMemory.objects.create(

            user_message=user_message,

            jarvis_reply=reply

        )



        return JsonResponse({

            "reply": reply

        })