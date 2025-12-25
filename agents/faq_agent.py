from logic_blocks.benefits import benefits_block
from logic_blocks.usage import usage_block
from logic_blocks.safety import safety_block
import json

def run(state):
    product = state["product"]
    faqs = [
        {"q": "What does this serum do?", "a": benefits_block(product)},
        {"q": "How do I use it?", "a": usage_block(product)},
        {"q": "Is it safe?", "a": safety_block(product)},
        {"q": "Who can use this?", "a": "Suitable for oily and combination skin."},
        {"q": "When should I apply it?", "a": "Morning routine before sunscreen."}
    ]

    with open("outputs/faq.json", "w") as f:
        json.dump({"page": "FAQ", "items": faqs}, f, indent=2)

    return state
