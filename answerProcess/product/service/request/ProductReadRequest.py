from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductReadRequest:
    __productNumber: int

    def getProductNumber(self):
        return self.__productNumber