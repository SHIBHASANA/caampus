from django import forms
from .models import Product, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ["seller"]

        widgets = {

            "title": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter product title"
            }),

            "category": forms.Select(attrs={
                "class": "form-select form-select-lg"
            }),

            "college": forms.Select(attrs={
                "class": "form-select form-select-lg"
            }),

            "price": forms.NumberInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "₹ Enter price"
            }),

            "condition": forms.Select(attrs={
                "class": "form-select form-select-lg"
            }),

            "department": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Department"
            }),

            "semester": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Semester"
            }),

            "subject": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Subject"
            }),

            "stock": forms.NumberInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Available Stock"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Describe your product..."
            }),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "negotiable": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review

        fields = ["rating", "comment"]

        widgets = {

            "rating": forms.Select(
                choices=[
                    (1, "⭐"),
                    (2, "⭐⭐"),
                    (3, "⭐⭐⭐"),
                    (4, "⭐⭐⭐⭐"),
                    (5, "⭐⭐⭐⭐⭐"),
                ],
                attrs={
                    "class": "form-select"
                }
            ),

            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Write your review..."
                }
            ),
        }