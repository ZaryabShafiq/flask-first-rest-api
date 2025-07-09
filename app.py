from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data: a list of product dicts
products = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Mouse", "price": 25},
    {"id": 3, "name": "Keyboard", "price": 45}
    
]

# Route: GET all products
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({"products": products}), 200

# Route: GET single product by id
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

# Route: POST add new product
@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_id = max(p["id"] for p in products) + 1
    new_product = {
        "id": new_id,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == "__main__":
    app.run(debug=True)
