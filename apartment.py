import random as r
from marshmallow import Schema, fields, post_load


class Apartment:
    def __init__(self, host_name="jack"):
        self.price = None
        self.area = None
        self.rate = None
        self.host_name = host_name
        self.randomise()

    def randomise(self):
        self.price = r.randint(100, 1000000000000000000)
        self.area = r.randint(4, 10000)
        self.rate = r.uniform(0, 100)


class ApartmentSchema(Schema):
    price = fields.Integer()
    area = fields.Integer()
    rate = fields.Float()

    @post_load
    def make_user(self, data, **kwargs):
        return Apartment(**data)

