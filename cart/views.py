from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Cart
from products.models import Product


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)

    total = sum(item.total_price() for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total": total,
    }

    return render(request, "cart.html", context)


from django.shortcuts import render


@login_required
def increase_quantity(request, cart_id):
    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        user=request.user
    )

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')


@login_required
def decrease_quantity(request, cart_id):
    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        user=request.user
    )

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


@login_required
def remove_cart(request, cart_id):
    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        user=request.user
    )

    cart_item.delete()

    return redirect('cart')
# Create your views here.
from django.shortcuts import render

# Create your views here.
