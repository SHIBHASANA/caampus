from django.db import models
from django.contrib.auth.models import User
from accounts.models import College


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')
    description = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Like New', 'Like New'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
    ]
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES
    )
    department = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    subject = models.CharField(max_length=100, blank=True)
    negotiable = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"


class Banner(models.Model):
    title = models.CharField(max_length=200)

    subtitle = models.CharField(max_length=300)

    image = models.ImageField(upload_to='banners/')

    button_text = models.CharField(max_length=50)

    button_link = models.CharField(max_length=200, default="#")

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
