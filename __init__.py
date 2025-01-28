from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    products = dao.list_products()
    result = []
    for product in products:
        result.append(Product.load(product))

    return result



def get_product(product_id: int) -> Product:
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)

def get_products_batch(product_ids: list[int]) -> list[Product]:

    # Fetch product details for all IDs from the DAO
    products_data = dao.get_products_batch(product_ids)

    # Convert each product dictionary into a Product object
    products = [Product.load(product_data) for product_data in products_data]

    return products

