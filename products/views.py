from .forms import ProductForm, ReviewForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Category, Banner, Review
from django.db.models import Q, Sum, Avg, Count
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta


def home(request):
    banners = Banner.objects.filter(is_active=True)

    categories = Category.objects.filter(status=True)

    products = Product.objects.filter(
        is_available=True
    ).annotate(

        # Average rating
        average_rating=Avg(
            "reviews__rating"
        ),

        # Number of reviews
        review_count=Count(
            "reviews"
        ),

        # Wishlist count
        wishlist_count=Count(
            "wishlist_items"
        )

    )

    # Get filter values

    category = request.GET.get('category')
    department = request.GET.get('department')
    semester = request.GET.get('semester')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Apply filters

    if category:
        products = products.filter(
            category_id=category
        )

    if department:
        products = products.filter(
            department=department
        )

    if semester:
        products = products.filter(
            semester=semester
        )

    if min_price:
        products = products.filter(
            price__gte=min_price
        )

    if max_price:
        products = products.filter(
            price__lte=max_price
        )

    products = products.order_by(
        '-created_at'
    )

    # Badge checking

    for product in products:
        # New product within 7 days

        product.is_new = (
                product.created_at >=
                timezone.now() - timedelta(days=7)
        )

        # Best seller based on wishlist

        product.is_best_seller = (
                product.wishlist_count >= 10
        )

    departments = Product.objects.values_list(
        'department',
        flat=True
    ).distinct()

    semesters = Product.objects.values_list(
        'semester',
        flat=True
    ).distinct()

    context = {

        'banners': banners,

        'categories': categories,

        'products': products,

        'departments': departments,

        'semesters': semesters,

    }

    return render(
        request,
        'index.html',
        context
    )


def product_details(request, id):
    product = get_object_or_404(
        Product,
        id=id
    )

    if request.method == "POST":

        if request.user.is_authenticated:

            form = ReviewForm(
                request.POST
            )

            if form.is_valid():
                review = form.save(
                    commit=False
                )

                review.user = request.user

                review.product = product

                review.save()

                return redirect(
                    "product_details",
                    id=product.id
                )


    else:

        form = ReviewForm()

    reviews = Review.objects.filter(
        product=product
    ).order_by(
        "-created_at"
    )

    average = reviews.aggregate(
        Avg("rating")
    )["rating__avg"]

    related_products = Product.objects.filter(
        category=product.category,
        is_available=True
    ).exclude(
        id=id
    )[:4]

    context = {

        "product": product,

        "related_products": related_products,

        "reviews": reviews,

        "form": form,

        "average": average,

    }

    return render(
        request,
        "product_details.html",
        context
    )


def search_products(request):
    query = request.GET.get('q')

    products = Product.objects.filter(
        is_available=True
    ).annotate(

        average_rating=Avg(
            "reviews__rating"
        )

    )

    if query:
        products = products.filter(

            Q(title__icontains=query) |

            Q(subject__icontains=query) |

            Q(department__icontains=query) |

            Q(category__name__icontains=query)

        )

    return render(

        request,

        'search_results.html',

        {
            'products': products,
            'query': query
        }

    )


@login_required
def my_products(request):
    products = Product.objects.filter(
        seller=request.user
    )

    return render(

        request,

        "my_products.html",

        {
            "products": products
        }

    )


@login_required
def add_product(request):
    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            product = form.save(
                commit=False
            )

            product.seller = request.user

            product.save()

            return redirect(
                'my_products'
            )


    else:

        form = ProductForm()

    return render(

        request,

        "add_product.html",

        {
            "form": form
        }

    )


@login_required
def edit_product(request, id):
    product = get_object_or_404(

        Product,

        id=id,

        seller=request.user

    )

    if request.method == "POST":

        form = ProductForm(

            request.POST,

            request.FILES,

            instance=product

        )

        if form.is_valid():
            form.save()

            return redirect(
                'my_products'
            )


    else:

        form = ProductForm(
            instance=product
        )

    return render(

        request,

        "edit_product.html",

        {
            "form": form
        }

    )


@login_required
def delete_product(request, id):
    product = get_object_or_404(

        Product,

        id=id,

        seller=request.user

    )

    if request.method == "POST":
        product.delete()

        return redirect(
            "my_products"
        )

    return render(

        request,

        "delete_product.html",

        {
            "product": product
        }

    )


@login_required
def seller_dashboard(request):
    products = Product.objects.filter(
        seller=request.user
    )

    total_products = products.count()

    total_stock = products.aggregate(

        Sum("stock")

    )["stock__sum"] or 0

    context = {

        "products": products,

        "total_products": total_products,

        "total_stock": total_stock,

    }

    return render(

        request,

        "seller_dashboard.html",

        context

    )


from django.shortcuts import render

# Create your views here.
