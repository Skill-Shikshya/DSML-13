class TransactionError(Exception):
    pass


class InvalidAgeException(Exception):
    """Raised when the input value is less than 18"""
    pass