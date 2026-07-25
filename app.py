from flask import Flask, jsonify
from db import connection
from cache import cache
from decimal import Decimal
import json

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "ShopSphere API",
        "version": "3.0",
        "message": "MySQL + Redis"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/products")
def products():

    cached_products = cache.get("products")

    if cached_products:
        print("Cache HIT")
        return jsonify(json.loads(cached_products))

    print("Cache MISS")

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    cursor.close()

    # Convert Decimal to float
    for item in data:
        if isinstance(item["price"], Decimal):
            item["price"] = float(item["price"])

    cache.setex(
        "products",
        60,
        json.dumps(data)
    )

    return jsonify(data)

    # Check Redis Cache
    cached_products = cache.get("products")

    if cached_products:
        print("Cache HIT")
        return jsonify(json.loads(cached_products))

    print("Cache MISS")

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    cursor.close()

    # Save to Redis (60 seconds)
    cache.setex(
        "products",
        60,
        json.dumps(data)
    )

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
