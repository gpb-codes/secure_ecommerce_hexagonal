class DomainError(Exception):
    pass


class ProductNotFound(DomainError):
    pass


class InvalidProduct(DomainError):
    pass
