from fastapi import APIRouter, Query, Path
from models.product import Product

router = APIRouter()

products = [{
    "id": 1,
    "name": "laptop",
    "price": 800,
    "quantity": 4
    },
    {
        "id": 2,
        "name": "monitor",
        "price": 800,
        "quantity": 4
    }]


@router.get("/products")
def get_products():
    return products

@router.get("/products/{id}")
def get_products(id: int = Path(gt=0)):
    return list(filter(lambda product: product['id'] == id, products))

@router.get("/products/")
def get_products_by_quantity(quantity: int, price: float = Query(gt=0, le=1000)):
    return list(filter(lambda product: product['quantity'] == quantity and product['price'] == price, products))

@router.post("/products")
def create_product(product: Product):
    products.append(product)
    return products

@router.put("/products/{id}")
def update_product(id: int, product: Product):
    for i, item in enumerate(products):
        if item['id'] == id:
            products[i]['name'] = product.name 
            products[i]['price'] = product.price 
            products[i]['quantity'] = product.quantity 
            break
    return products

@router.delete("/products/{id}")
def delete_product(id: int):
    for product in products:
        if product['id'] == id:
            products.remove(product)
            break
    return products