from email.policy import default
from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ("Category1", "Category1"),  # Category 1 option
    ("Category2", "Category2"),  # Category 2 option
    ("Category3", "Category3"),  # Category 3 option
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)  # Product name
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)  # Product category
    quantity = models.PositiveIntegerField(null=True)  # Product quantity
    description = models.CharField(max_length=200, null=True)  # Product description

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)  # Ordered product
    created_by = models.ForeignKey(User, models.CASCADE, null=True)  # User who created the order
    order_quantity = models.PositiveIntegerField(null=True)  # Ordered quantity
    date = models.DateTimeField(auto_now_add=True)  # Order creation date and time

    def __str__(self) -> str:
        return f"{self.product} ordered quantity {self.order_quantity}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address = models.CharField(max_length=40, null=True)  # User's physical address
    mobile = models.CharField(max_length=12, null=True)  # User's mobile number
    picture = models.ImageField(default="avatar.jpeg", upload_to="Pictures")  # User's profile picture

    def __str__(self) -> str:
        return self.user.username
