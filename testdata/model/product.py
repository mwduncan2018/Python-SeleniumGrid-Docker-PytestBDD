from dataclasses import dataclass

@dataclass
class Product:
    manufacturer: str 
    model: str 
    price: int 
    number_in_stock: int