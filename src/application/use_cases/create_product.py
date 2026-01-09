
class CreateProduct:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, name: str, price: float, stock: int) -> Product:
        product = Product.create(name, price, stock)
        return self.repository.save(product)
