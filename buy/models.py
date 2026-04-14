from django.db import models
from product.models import Product

# Data model Buy
class Buy(models.Model):
    client = models.CharField(max_length=20, verbose_name="Name client")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product")

    def __str__(self):
        return f"Producto {self.product} comprado por {self.client}"

    # Client make the shop a product
    def make_shop(name):
        product_buy = input("Indique el Producto que quiere comprar ")
        buy = Buy.objects.create(client=name, product=product_buy)

        buy.save()
        print(f"El cliente {name} ha comprado el Producto {product_buy}")

    # Client request a Product's availability
    def products_availability():
        product = Product.objects.filter(availability=True)

        print(f"Los productos que estan disponibles son {product}")

    # Client cancel Buy
    def cancel_buy(name):
        buy = Buy.objects.get(client=name)

        buy.delete()

        print(f"El cliente {name} cancelo su compra")