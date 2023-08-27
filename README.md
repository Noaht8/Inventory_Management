# Inventory Management System

This is an Inventory Management System built using Python Django. It allows users to manage their inventory, create products, place orders, and update their profile information. The system also provides an admin interface to manage orders and products.

## Installation

Follow these steps to set up the project:

1. Create a virtual environment:
   ```
   python -m venv myvenv
   ```

2. Activate the virtual environment:

   On Windows:
   ```
   $ env\Scripts\activate
   ```

   On Linux/Mac:
   ```
   $ source /env/bin/activate
   ```

3. Install necessary libraries:
   ```
   pip install django
   pip install django-crispy-forms
   pip install crispy-bootstrap5
   python -m pip install Pillow
   ```

4. Create the Django project:
   ```
   django-admin startproject DjangoProject
   ```

5. Change directory to DjangoProject:
   ```
   cd DjangoProject
   ```

6. Create the inventory app:
   ```
   python manage.py startapp inventoryApp
   ```

## Functional Requirements

1. User Registration: The code allows users to register an account by providing necessary information such as username, password, and any additional fields defined in the UserRegistry form.

2. User Login: The code allows registered users to log in to their accounts using their credentials.

3. User Logout: The code provides a mechanism for users to log out of their accounts.

4. Product Listing: The "products" view displays a list of all products in the system.

5. Product Creation: Authenticated users can create new products by submitting the required information through the ProductForm.

6. Product Update: Authenticated users can update existing products by submitting the modified information through the ProductForm.

7. Order Placement: The "orders" view allows authenticated users to place orders by submitting the required information through the OrderForm.

8. Order Listing: The "orders" view displays a list of all orders placed by the authenticated user.

9. Order Management: Administrators can view and manage all orders placed by users, including updating the order status and other relevant information.

10. User Profile Update: Authenticated users can update their profile information, such as physical address, mobile number, and profile picture.

## Usage

To run the project, navigate to the project directory and execute the following command:

```
python manage.py runserver
```

Then, open your web browser and visit `http://localhost:8000` to access the Inventory Management System.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
