from logic_blocks import benefits, usage, ingredients, pricing
import json

def run(state):
    product = state["product"]
    page = {
        "name": product["name"],
        "description": benefits.benefits_block(product),
        "ingredients": ingredients.ingredients_block(product),
        "usage": usage.usage_block(product),
        "price": pricing.pricing_block(product)
    }

    with open("outputs/product_page.json", "w") as f:
        json.dump(page, f, indent=2)

    return state
