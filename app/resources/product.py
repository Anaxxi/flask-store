from flask_restful import Resource, marshal_with, marshal

from app.models import Product
from app.schemas import product_fields

class ProductList(Resource):

    @marshal_with(product_fields, "products")
    def get(self):
        products = Product.query.all()
        return products

class ProductGet(Resource):


    def get(self, slug):
        product = Product.query.filter_by(slug=slug).first()
        if not product:
            return {"message":"Product not found"}, 400

        return marshal(product, product_fields, "product")
