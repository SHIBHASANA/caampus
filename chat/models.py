from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Conversation(models.Model):
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="buyer_conversations"
    )

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="seller_conversations"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.product.title}"


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages"
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.sender.username

    class Message(models.Model):
        conversation = models.ForeignKey(
            Conversation,
            on_delete=models.CASCADE
        )

        sender = models.ForeignKey(
            User,
            on_delete=models.CASCADE
        )

        message = models.TextField()

        timestamp = models.DateTimeField(
            auto_now_add=True
        )

        is_read = models.BooleanField(
            default=False
        )

        def __str__(self):
            return self.message

