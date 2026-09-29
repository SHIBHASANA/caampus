from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    if request.method == "POST":

        phone = request.POST.get("phone")
        address = request.POST.get("address")

        for item in cart_items:
            Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity,
                total_price=item.product.price * item.quantity,
                phone=phone,
                address=address
            )

        cart_items.delete()

        return redirect("my_orders")

    context = {
        "cart_items": cart_items,
        "total": total
    }

    return render(request, "checkout.html", context)

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-ordered_at")

    return render(
        request,
        "my_orders.html",
        {
            "orders": orders
        }
    )