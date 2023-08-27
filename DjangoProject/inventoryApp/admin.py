from django.contrib import admin
from inventoryApp.models import Product, Order, UserProfile

admin.site.site_header = "Inventory Admin"

class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for managing the Product model in the admin interface.
    """
    model = Product
    list_display = ("name", "category", "quantity")  # Display these fields in the admin list view
    list_filter = ["category"]  # Enable filtering by category in the admin list view
    search_fields = ["name"]  # Enable searching by name in the admin list view

class OrderAdmin(admin.ModelAdmin):
    """
    Admin class for managing the Order model in the admin interface.
    """
    model = Order
    list_display = ("product", "created_by", "order_quantity", "date")  # Display these fields in the admin list view
    list_filter = ["date"]  # Enable filtering by date in the admin list view
    search_fields = ["product"]  # Enable searching by product in the admin list view

class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin class for managing the UserProfile model in the admin interface.
    """
    model = UserProfile
    list_display = ("user", "physical_address", "mobile", "picture")  # Display these fields in the admin list view
    list_filter = ["user"]  # Enable filtering by user in the admin list view
    search_fields = ["user"]  # Enable searching by user in the admin list view

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(UserProfile, UserProfileAdmin)