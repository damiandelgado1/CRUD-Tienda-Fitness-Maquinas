from django.db import models

# Data model Product
class Product(models.Model):
    name = models.TextField(null=True, verbose_name="Name Product")
    brand = models.TextField(null=True, verbose_name="Brand Product")
    type = models.TextField(null=True, verbose_name="Type product")
    stock = models.IntegerField(verbose_name="Stock availability Product")
    availability = models.BooleanField(verbose_name="Availability")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Nuevo producto a la venta {self.name} {self.brand} {self.stock}"

    # Register product's in the Shop to Sale's
    def create_product(name, brand, type, stock, availability, price):
        product = Product.objects.create(name=name, brand=brand, type=type, stock=stock, availability=availability, price=price)

        product.save()
        print(f"Nuevo producto a la Venta")

    # Modify stock a Product
    def modify_product(id, stock):
        product = Product.objects.get(pk=id)
        product.stock = stock
        product.update()

        print(f"Producto {product}")

    # Delete Prodcut by shop
    def delete_product(name):
        product = Product.objects.filter(name=name)
        product.delete()

        print(f"Producto {product} eliminado de la Tienda")