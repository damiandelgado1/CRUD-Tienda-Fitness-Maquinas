# CRUD-Tienda-Fitness-Maquinas

### description
Backend CRUD Project manage the product's in the Shop Fitness and client purchased of Product, this project is a Backend with CRUD methods by ORM methods in the Django Shell for manage product in DataBase and Buy's client

### features

App Product's
- Create new product for Sale's in Shop
- Modify stock availability of Product
- Delete product by Shop

App Buy
- Client make a purchase Product
- Client request a Product availability
- Client cancel a purchase

The DataBase created in local with a connection via Extension's

### structure project

```text
shop_product/          # Project 1: Main Project of Product Shop
|
|-- settings.py        # Config main
|
|-- product/           # App 1: Data product for Sales
|   |
|   |-- models.py      # Information and Managment of the Product in the Shop
|
|-- buy/               # App 2: Data about the Shop
|   |
|   |-- models.py      # Creation, Delete and Data of the Buy
|
|-- database           # DataBase 1: Product's data and User request interaction
|   |...
|
|-- manage.py
