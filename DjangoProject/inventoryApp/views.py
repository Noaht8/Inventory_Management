from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from inventoryApp.forms import UserRegistry, ProductForm, OrderForm
from inventoryApp.models import Product, Order
from django.contrib import messages



@login_required
def index(request):
    """
    View function for the index page.
    
    Retrieves order for the current user, first two users, first two orders,
    first two products, and counts the number of registered users, products, and orders.
    
    Also retrieves the registered session value and renders the index template with the context data.
    """
    # Retrieve orders for the current user
    orders_user = Order.objects.all()

    # Retrieve the first two users
    users = User.objects.all()[:2]

    # Retrieve the first two orders
    orders_adm = Order.objects.all()[:2]

    # Retrieve the first two products
    products = Product.objects.all()[:2]

    # Count the number of registered users
    reg_users = len(User.objects.all())

    # Count the number of products
    all_prods = len(Product.objects.all())

    # Count the number of orders
    all_orders = len(Order.objects.all())

    # Get the registered session value
    registered = request.session.get('registered')

    # Prepare the context data
    context = {
        "title": "Home",
        "orders": orders_user,
        "orders_adm": orders_adm,
        "users": users,
        "products": products,
        "count_users": reg_users,
        "count_products": all_prods,
        "count_orders": all_orders,
        "registered": registered,
    }

    # Render the index template with the context data
    return render(request, "inventory/index.html", context)



def register(request):
    """
    View function for the registration page.
    
    Handles the user registration form submission, saves the form if valid,
    sets the 'registered' session value to True, and redirects to the login page.
    
    Renders the register template with the registration form.
    """
    if request.method == "POST":
        # Handle the user registration form submission
        form = UserRegistry(request.POST)
        if form.is_valid():
            form.save()
            request.session['registered'] = True
            return redirect("login")
    else:
        form = UserRegistry()

    # Prepare the context data
    context = {"register": "Register", "form": form}

    # Render the register template with the context data
    return render(request, "inventory/register.html", context)

@login_required
def products(request):
    """
    View function for the products page.

    Retrieves all products, handles the product form submission,
    saves the form if valid, and redirects to the products page.

    Renders the products template with the products and product form.
    """
    # Retrieve all products
    products = Product.objects.all()

    if request.method == "POST":
        # Handle the product form submission
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()

    # Prepare the context data
    context = {"title": "Products", "products": products, "form": form}

    # Render the products template with the context data
    return render(request, "inventory/products.html", context)


@login_required
def orders(request):
    """
    View function for the orders page.
    
    Retrieves all orders, gets the value of the 'my_cookie' cookie,
    handles the order form submission, saves the form if valid,
    and redirects to the orders page.
    
    Renders the orders template with the orders, order form, and 'my_cookie' value.
    """
    # Retrieve all orders
    orders = Order.objects.all()

    # Get the value of the 'my_cookie' cookie
    my_cookie = request.COOKIES.get('my_cookie')

    if request.method == "POST":
        # Handle the order form submission
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect("orders")
    else:
        form = OrderForm()

    # Prepare the context data
    context = {"title": "Orders", "orders": orders, "form": form, "my_cookie": my_cookie}

    # Render the orders template with the context data
    return render(request, "inventory/orders.html", context)


@login_required
def users(request):
    """
    View function that retrieves all users and renders the users template.

    Args:
    request: The HTTP request object.

    Returns:
    A rendered HTML template with the context data containing the title and users.
    """
    # Retrieve all users
    users = User.objects.all()

    # Prepare the context data
    context = {"title": "Users", "users": users}

    # Render the users template with the context data
    return render(request, "inventory/users.html", context)


@login_required
def user(request):
    """
    View function that renders the user profile template and sets a cookie.

    Args:
    request: The HTTP request object.

    Returns:
    A rendered HTML template with the context data containing the user profile.
    """
    # Prepare the context data
    context = {"profile": "User Profile"}

    # Create a response object
    response = render(request, "inventory/user.html", context)

    # Set the 'my_cookie' cookie
    response.set_cookie('my_cookie', 'cookie_value')

    # Return the response
    return response


@login_required
def edit_product(request, product_id):
    """
    Edit a product.

    Args:
        request: The HTTP request object.
        product_id: The ID of the product to be edited.

    Returns:
        If the request method is POST and the form is valid, redirects to the "products" page.
        Otherwise, renders the "edit_product.html" template with the product form.

    """
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm(instance=product)
    context = {"title": "Edit Product", "form": form}
    return render(request, "inventory/edit_product.html", context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product.

    Args:
        request: The HTTP request object.
        product_id: The ID of the product to be deleted.

    Returns:
        Redirects to the "products" page after deleting the product.

    """
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully.")
    return redirect("products")


@login_required
def edit_order(request, order_id):
    """
    Edit an order.

    Args:
        request: The HTTP request object.
        order_id: The ID of the order to be edited.

    Returns:
        If the request method is POST and the form is valid, redirects to the "orders" page.
        Otherwise, renders the "edit_order.html" template with the order form.

    """
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("orders")
    else:
        form = OrderForm(instance=order)
    context = {"title": "Edit Order", "form": form}
    return render(request, "inventory/edit_order.html", context)


@login_required
def delete_order(request, order_id):
    """
    Delete an order.

    Args:
        request: The HTTP request object.
        order_id: The ID of the order to be deleted.

    Returns:
        Redirects to the "orders" page after deleting the order.

    """
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        order.delete()
        messages.success(request, "Order deleted successfully.")
    return redirect("orders")
