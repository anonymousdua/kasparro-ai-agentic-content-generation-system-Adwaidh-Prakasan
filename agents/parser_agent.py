def run(state):
    raw = state["raw_product_data"]
    state["product"] = {
        "name": raw["Product Name"],
        "concentration": raw["Concentration"],
        "skin_type": raw["Skin Type"],
        "ingredients": raw["Key Ingredients"],
        "benefits": raw["Benefits"],
        "usage": raw["How to Use"],
        "side_effects": raw["Side Effects"],
        "price": raw["Price"]
    }
    return state
