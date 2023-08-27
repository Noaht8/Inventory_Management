from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from inventoryApp.models import Product, Order


class UserRegistry(UserCreationForm):
    """
    Inherits from UserCreationForm, which is a built-in form provided by Django for user registration.
    Adds an email field to the form.

    Attributes:
    email (forms.EmailField): Field for user email.

    Meta:
    model (User): The User model to be used for user registration.
    fields (list): The fields to be included in the form.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2",]


class ProductForm(forms.ModelForm):
    """
    A form for creating and updating product information.

    Inherits from ModelForm, which is a built-in form provided by Django for model-based forms.
    Represents the Product model.

    Meta:
    model (Product): The Product model to be used for the form.
    fields (list): The fields to be included in the form.
    """
    class Meta:
        model = Product
        fields = ["name", "category", "quantity", "description"]


class OrderForm(forms.ModelForm):
    """
    A form for creating and updating order information.

    Inherits from ModelForm, which is a built-in form provided by Django for model-based forms.
    Represents the Order model.

    Meta:
    model (Order): The Order model to be used for the form.
    fields (list): The fields to be included in the form.
    """
    class Meta:
        model = Order
        fields = ["product", "order_quantity"]
