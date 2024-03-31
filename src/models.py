import json


class Product:

    def __init__(self, id: int, name: str, url: str, price: str, disc_price: int, brand: str):
        self.id = id
        self.name = name
        self.url = 'https://online.metro-cc.ru' + url
        self.price = price
        self.disc_price = disc_price
        self.brand = brand

    def as_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'price': self.price,
            'disc_price': self.disc_price,
            'brand': self.brand
        }
