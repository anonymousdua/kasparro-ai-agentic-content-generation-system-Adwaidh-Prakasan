from config import client, MODEL
import json

def run(state):
    product = state["product"]

    prompt = f"""You are an agent generating user questions based on product data.

Use ONLY the following product data:

{json.dumps(product, indent=2)}

Generate at least 15 categorized user questions about this product.
Organize questions into these categories: Informational, Usage, Safety, Purchase, Comparison.

You MUST return ONLY a valid JSON object with no other text. The JSON structure should be:
{{
  "Informational": ["question1", "question2", ...],
  "Usage": ["question1", "question2", ...],
  "Safety": ["question1", "question2", ...],
  "Purchase": ["question1", "question2", ...],
  "Comparison": ["question1", "question2", ...]
}}

Start your response with {{ and end with }}. No markdown, no extra text."""

    res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    response_text = res.choices[0].message.content.strip()
    
    # Try to parse JSON, with error handling
    try:
        state["questions"] = json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print(f"Response was: {response_text[:500]}")
        raise
    
    return state
