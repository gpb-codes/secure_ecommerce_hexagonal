class DomainError(Exception):
    pass


class ProductNotFoundError(DomainError):
    pass


class InvalidProductDataError(DomainError):
    pass
