from dataclasses import dataclass


@dataclass
class PriceRecord:
    """
    Represents a price record.
    """

    product: str
    price: float
