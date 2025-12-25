def comparison_block(product, product_b):
    return {
        "ingredients": {
            "glowboost": product["ingredients"],
            "product_b": product_b["ingredients"]
        },
        "price": {
            "glowboost": product["price"],
            "product_b": product_b["price"]
        }
    }
