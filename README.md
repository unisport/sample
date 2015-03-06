Getting started:

    # Install needed python packages.
    pip install -r requirements.txt

    # Create database and tables.
    python manage syncdb

    # Sync database with the data from the API sample.
    python manage.py syncdata

    # Start the Django server.
    python manage.py runserver

Usage:

    # List all products, 10 products per page
    # and sorted by price with cheapest first.
    GET /products/

    # List products for kids, 10 products per page
    # and sorted by price with cheapest first.
    GET /products/kids/

    # Show the details for one product.
    GET /products/<pk>/

    # Delete the product with pk `<pk>`.
    GET /products/<pk>/delete/

    # Update data for the product with pk `<pk>`.
    GET /products/<pk>/update/

    # Create a new product.
    GET /products/create/
