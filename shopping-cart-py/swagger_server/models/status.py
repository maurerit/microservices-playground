from enum import Enum, unique


@unique
class ShoppingCartStatus(Enum):
    SHOPPING = 0
    ORDERED = 1
    IN_PROGRESS = 2
    GATHERING_MATERIALS = 3
    SHIPPING = 4
    COMPLETE = 5
