from logic_blocks.comparison import comparison_block
import json

def run(state):
    product_b = {
        "name": "RadiantFix C Serum",
        "ingredients": ["Vitamin C", "Niacinamide"],
        "benefits": ["Glow", "Even tone"],
        "price": 799
    }

    comparison = comparison_block(state["product"], product_b)

    with open("outputs/comparison_page.json", "w") as f:
        json.dump(comparison, f, indent=2)

    return state
