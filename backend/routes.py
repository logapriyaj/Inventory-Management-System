from flask import Blueprint, jsonify

routes = Blueprint('routes', __name__)

@routes.route('/products')
def get_products():
    return jsonify([
        {"id": 1, "name": "Laptop", "stock": 10},
        {"id": 2, "name": "Mouse", "stock": 50}
    ])
