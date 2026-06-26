from django.db import models


class ChatMemory(models.Model):

    user_message = models.TextField()

    jarvis_reply = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.user_message
