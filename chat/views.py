from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Conversation, Message
from .forms import MessageForm


@login_required
def start_chat(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    # Prevent chatting with yourself
    if product.seller == request.user:
        return redirect(
            "product_details",
            id=product.id
        )

    conversation, created = Conversation.objects.get_or_create(
        buyer=request.user,
        seller=product.seller,
        product=product
    )

    return redirect(
        "chat_room",
        conversation_id=conversation.id
    )


@login_required
@login_required
def chat_list(request):
    conversations = Conversation.objects.filter(
        buyer=request.user
    ) | Conversation.objects.filter(
        seller=request.user
    )

    conversations = conversations.order_by("-created_at")

    for conversation in conversations:
        # Last message
        conversation.last_message = Message.objects.filter(
            conversation=conversation
        ).order_by("-timestamp").first()

        # Unread count
        conversation.unread_count = Message.objects.filter(
            conversation=conversation,
            is_read=False
        ).exclude(
            sender=request.user
        ).count()

    return render(
        request,
        "chat/chat_list.html",
        {
            "conversations": conversations
        }
    )


@login_required
def chat_room(request, conversation_id):
    conversation = get_object_or_404(
        Conversation,
        id=conversation_id
    )

    # Security check
    if request.user not in [
        conversation.buyer,
        conversation.seller
    ]:
        return redirect("/")

    # Mark received messages as read

    Message.objects.filter(
        conversation=conversation
    ).exclude(
        sender=request.user
    ).update(
        is_read=True
    )

    # Send message

    if request.method == "POST":

        form = MessageForm(
            request.POST
        )

        if form.is_valid():
            message = form.save(
                commit=False
            )

            message.conversation = conversation

            message.sender = request.user

            message.save()

            return redirect(
                "chat_room",
                conversation_id=conversation.id
            )



    else:

        form = MessageForm()

    messages = Message.objects.filter(
        conversation=conversation
    ).order_by(
        "timestamp"
    )

    # Sidebar conversations

    conversations = Conversation.objects.filter(
        buyer=request.user
    ) | Conversation.objects.filter(
        seller=request.user
    )

    conversations = conversations.order_by(
        "-created_at"
    )

    return render(
        request,
        "chat/chat_room.html",
        {
            "conversation": conversation,
            "messages": messages,
            "form": form,
            "conversations": conversations,
        }
    )