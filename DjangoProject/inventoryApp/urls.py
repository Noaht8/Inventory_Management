# Importing necessary modules
from django.urls import path
from inventoryApp import views

# Defining URL patterns
urlpatterns = [
    path("dash/", views.index, name="dash"),  # URL for dashboard
    path("products/", views.products, name="products"),  # URL for products page
    path("orders/", views.orders, name="orders"),  # URL for orders page
    path("users/", views.users, name="users"),  # URL for users page
    path("user/", views.user, name="user"),  # URL for user page
    path("register/", views.register, name="register"),  # URL for registration page
    path("edit_product/<int:product_id>/", views.edit_product, name="edit_product"),  # URL for editing a product
    path("delete_product/<int:product_id>/", views.delete_product, name="delete_product"),  # URL for deleting a product
    path("edit_order/<int:order_id>/", views.edit_order, name="edit_order"),  # URL for editing an order
    path("delete_order/<int:order_id>/", views.delete_order, name="delete_order"),  # URL for deleting an order
]